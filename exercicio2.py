n1= float(input("Digite a primerira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1+n2+n3+n4) / 4

if (media >= 7):
    print("A sua media foi", media, "você está Aprovado")
else:
    print("A sua media foi", media, "você está Reprovado")
