def obter_chaves():
    dicionario = {}
    while True:
        chave = input("Digite a chave (ou 'fim' para encerrar): ")
        if chave == 'fim':
            break
        valor = input("Digite o valor: ")
        dicionario[chave] = valor
    chaves = list(dicionario.keys())
    return chaves

# Exemplo de uso
chaves = obter_chaves()
print(f"A lista de chaves é: {chaves}")
