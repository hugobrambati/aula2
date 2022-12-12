idade = int(input("Informe sua idade: "))
if (idade < 18):
    print("Menor de Idade")
elif (idade >= 18 and idade < 65):
    print("Adulto")
else:
    print("3ª idade")