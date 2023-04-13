
def chave_maior_valor(dicionario):
    chave_maxima = None
    valor_maximo = float('-inf')
    for chave, valor in dicionario.items():
        if valor > valor_maximo:
            chave_maxima = chave
            valor_maximo = valor
    return chave_maxima

dicionario = {}
n = int(input("Quantos números deseja inserir no dicionário? "))
for i in range(n):
    chave = input(f"Informe a chave para o número {i+1}: ")
    valor = int(input(f"Informe o valor para a chave '{chave}': "))
    dicionario[chave] = valor

chave_maxima = chave_maior_valor(dicionario)

print(f"A chave com o maior valor é '{chave_maxima}'")
