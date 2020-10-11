"""
Esse algoritmo tera como entradas:

- padrao: sera um elementos da lista de palavras que foram processadas e geradas na etapa
          de preprocessamento (noise_removal, tokenization e normalization).

- texto: sera o conteudo em texto de um html preprocessado apenas na etapa de noise_removal.

Tera como retorno quais os indices na string do texto que deram match com o padrao.

"""

def rabin_karp(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q  # o %q evta o estouro do inteiro
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


# Driver Code
txt = "GEEKS FOR GEEKS"
pat = "GEEK"

# A prime number for hash function; this will reduce computation
q = 101

# numero de caracteres no alfabeto de entrada
d = 256

a = rabin_karp(txt, pat, d, q)
print("[RABIN KARP] match positions: ", ",".join(a))
