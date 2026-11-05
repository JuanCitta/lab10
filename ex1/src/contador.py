def contar_palavras(texto):
    contagem = {}
    for palavra in texto.lower().split():
        palavra = palavra.strip(".,;:!?")
        if not palavra:
            continue
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem