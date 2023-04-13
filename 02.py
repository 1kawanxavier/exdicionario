def filtrar_idade_maior_que_18(nome, idade):
    if idade > 18:
        return {"idade": idade}
    else:
        return {}


nome = input("Informe o nome: ")
idade = int(input("Informe a idade: "))
resultado = filtrar_idade_maior_que_18(nome, idade)
print(f"O resultado é: {resultado}")
