"""
Esse algoritmo tera como entradas:

- padrao: sera um elementos da lista de palavras que foram processadas e geradas na etapa
          de preprocessamento (noise_removal, tokenization e normalization).

- texto: sera o conteudo em texto de um html preprocessado apenas na etapa de noise_removal.

Tera como retorno quais os indices na string do texto que deram match com o padrao.

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


# Driver Code
txt = "GEEKS FOR GEEKS"
pat = "GEEK"

a = brute_force(txt, pat)
print("[BRUTE FORCE] match positions: ", ",".join(a))
