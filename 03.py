def criar_dicionario():
    chaves = input("Digite as chaves separadas por espaço: ").split()
    valores = input("Digite os valores separados por espaço: ").split()
    dicionario = dict(zip(chaves, valores))
    return dicionario

dicionario = criar_dicionario()
print(f"O dicionário criado é: {dicionario}")
