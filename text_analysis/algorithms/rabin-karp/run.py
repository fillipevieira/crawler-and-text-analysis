"""
Esse algoritmo tera como entradas:

- padrao: sera um elementos da lista de palavras que foram processadas e geradas na etapa
          de preprocessamento (noise_removal, tokenization e normalization).

- texto: sera o conteudo em texto de um html preprocessado apenas na etapa de noise_removal.

Tera como retorno quais os indices na string do texto que deram match com o padrao.

Pontos negativos:
 - se o padrao tem um tamanho muito pequeno, tipo uma ṕalavra "e", o algoritmo sempre vai pegar janelas desse mesmo
   tamanho e, nesse caso, palavras com "e" no meio dariam matches sem ser exatamente a palavra isolada.

"""

def rabin_karp(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q  # o %q evita o estouro do inteiro
    p = 0
    t = 0
    result = []

    for i in range(m):  # preprocessamento
        p = (d*p+ord(pattern[i])) % q  # calcula o hash do padrao; ord() pega valor ascii do caracter
        t = (d*t+ord(text[i])) % q  # calcula o hash da primeira janela do texto

    for s in range(n-m+1):  # note o +1
        if p == t:  # faz checagem de caracter por caracter se true
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break

            if match:
                result = result + [str(s)]

        if s < n-m:
            t = (t-h*ord(text[s])) % q  # remove a letra s
            t = (t*d+ord(text[s+m])) % q  # adiciona a letra s+m
            t = (t+q) % q  # garante que t >= 0

    return result


if __name__ == "__main__":

    # Faz a leitura do arquivo que contem o texto preprocessado de um HTML
    with open("../../../preprocessed_files/pronounced-dead-michigan/noise-free-text.txt", "r") as file:
        text = file.read().lower()

    # Faz a leitura do arquivo que contem com as palavras preprocessadas de um HTML
    with open("../../../preprocessed_files/pronounced-dead-michigan/normalized-text.txt", "r") as file:
        words = [word.replace("\n", "") for word in file.readlines()]
        words = list(set(words))

    # Aplica o algoritmo utilizando o texto preprocessado de um HTML e cada palavra da lista de
    # palavras preprocessadas de um HTML
    matched_indexes_amount = 0
    for word in words:
        q = 101  # A prime number for hash function; this will reduce computation
        d = 256  # numero de caracteres no alfabeto de entrada
        matched_indexes = rabin_karp(text=text, pattern=word, d=d, q=q)
        if matched_indexes:
            matched_indexes_amount += 1

        print("[RABIN KARP ALGORITHM] Word: {} | Matched indexes: {}".format(word, ",".join(matched_indexes)))

    # Calcula similaridade
    words_amount = len(words)
    result = matched_indexes_amount / words_amount
    percent = result * 100

    print("\n------------------------- Results ---------------------------")
    print("Words amount: {}".format(str(words_amount)))
    print("Matched indexes amount: {}".format(str(matched_indexes_amount)))
    print("Similarity percentage: %.2f" % percent)
