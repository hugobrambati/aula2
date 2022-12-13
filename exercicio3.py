idade = int(input("Informe sua idade: "))

if(idade >= 5 and idade <= 7):
    print("Voce tem", idade, " anos sua categoria é a infantil A")
elif(idade >= 8 and idade <= 10):
    print("Voce tem", idade, "anos sua categoria é a infantil B")
elif(idade >= 11 and idade <= 13):
    print("Voce tem", idade, "anos sua categoria é a Juvenil A")
elif(idade >= 14 and idade <= 17):
    print("Voce tem", idade, "anos sua categoria é a Juvenil B")
elif(idade >= 18 and idade <= 65):
    print("Voce tem", idade, "anos sua Categoria é Adulto")
elif(idade >= 66 ):
    print("Voce tem", idade, "anos sua Categoria é Master")
else:
    print("Não temos categoria para sua idade")
