"""
Esse algoritmo tera como entradas:

- padrao: sera um elementos da lista de palavras que foram processadas e geradas na etapa
          de preprocessamento (noise_removal, tokenization e normalization).

- texto: sera o conteudo em texto de um html preprocessado apenas na etapa de noise_removal.

Tera como retorno quais os indices na string do texto que deram match com o padrao.

Pontos negativos:
 - se o padrao tem um tamanho muito pesqueno, tipo uma ṕalavra "e", o algoritmo sempre vai pegar janelas desse mesmo
   tamanho e, nesse caso, palavras com "e" no meio dariam matches sem ser exatamente a palavra isolada.

"""


def brute_force(text, pattern):
    integers = list()
    n_text = len(text)
    n_pattern = len(pattern)
    for i in range(n_text - n_pattern):
        j = 0

        while j < n_pattern and text[i+j] == pattern[j]:
            j += 1

        if j == n_pattern:
            integers.append(str(i))

    return integers


if __name__ == "__main__":

    # Faz a leitura do arquivo que contem o texto preprocessado de um HTML
    with open("../../preprocessing/noise-free-text.txt", "r") as file:
        text = file.read().lower()

    # Faz a leitura do arquivo que contem com as palavras preprocessadas de um HTML
    with open("../../preprocessing/normalized-text.txt", "r") as file:
        words = [word.replace("\n", "") for word in file.readlines()]
        words = list(set(words))

    # Aplica o algoritmo utilizando o texto preprocessado de um HTML e cada palavra da lista de
    # palavras preprocessadas de um HTML
    for word in words:
        matched_indexes = brute_force(text=text, pattern="e")
        print("[BRUTE FORCE ALGORITHM] Word: {} | Matched indexes: {}".format(word, ",".join(matched_indexes)))
