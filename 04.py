def separar_dicionario():
    dicionario = {}
    while True:
        chave = input("Digite a chave (ou 'fim' para encerrar): ")
        if chave == 'fim':
            break
        valor = input("Digite o valor: ")
        dicionario[chave] = valor
    chaves = list(dicionario.keys())
    valores = list(dicionario.values())
    return chaves, valores

chaves, valores = separar_dicionario()
print(f"A lista de chaves é: {chaves}")
print(f"A lista de valores é: {valores}")
