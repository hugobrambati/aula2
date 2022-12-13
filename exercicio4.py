cod = int(input("Digite o Codigo do funcionário: "))

if(cod == 101 or cod == 102 or cod == 103):
    sal = float(input("Digite o salário atual do funcionário: "))
    if (cod == 101):
        aum = sal * 10 / 100
        nsal = sal + aum
        dif = nsal - sal
        print("O Funcionário de codigo", cod, "que exerce a função de Gerente ganhou um aumento de 10%  passando de R$:", sal," para R$: ", nsal," com uma aumento de R$:", dif,".")
    elif (cod == 102):
        aum = sal * 20 / 100
        nsal = sal + aum
        dif = nsal - sal
        print("O Funcionário de codigo", cod, "que exerce a função de Engenheiro ganhou um aumento de 20%  passando de R$:", sal," para R$: ", nsal," com uma aumento de R$:", dif,".")
    elif (cod == 103):
        aum = sal * 30 / 100
        nsal = sal + aum
        dif = nsal - sal
        print("O Funcionário de codigo", cod, "que exerce a função de Tecnico ganhou um aumento de 30%  passando de R$:", sal," para R$: ", nsal," com uma aumento de R$:", dif,".")
else:
    print("Codigo não encontrado")