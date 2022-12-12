""" Tendo como dados de entrada a altura e o sexo de uma pessoa("M" masculino "F" feminino), construa um programa que
calcule seu peso ideal, utilizando as seguintes formulas:

- para homens: (72.7 * altura) - 58
- para mulheres: (62.1 * altura) - 44.7
"""

altura =float(input("Digite sua Altura: "))
sexo = input("Digite M para masculino e F para feminino: ")

if (sexo == "M" or sexo == "F"):
    if (sexo == "M"):
        peso_masculino = (72.7 * altura) - 58
        print(f"Seu peso ideal é de : {peso_masculino:.2f}") #:.2f e para colocar somente duas casas decimais
    if (sexo == "F"):
        peso_feminino = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é de: {peso_feminino:.2f}")
else:
    print("Porfavor digite M ou F")
