def obter_chaves_ordenadas():
    dicionario = {}
    while True:
        chave = input("Digite a chave (ou 'fim' para encerrar): ")
        if chave == 'fim':
            break
        valor = input("Digite o valor: ")
        dicionario[chave] = valor
    chaves_ordenadas = sorted(list(dicionario.keys()))
    return chaves_ordenadas


chaves_ordenadas = obter_chaves_ordenadas()
print(f"A lista de chaves ordenadas é: {chaves_ordenadas}")
