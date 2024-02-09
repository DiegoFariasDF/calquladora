import math

opcao = 1
while(opcao!='0'):
    opcao=input("Qual operação?: \n Soma(+) \n Subtração(-) \n Multiplicação(*) \n Divisão(/) \n Expoente(**) \n Raiz(r)\n")
    if(opcao == '+'):
        valor1 = float(input("Digite o primeiro valor"))
        valor2 = float(input("Digite o Segundo valor"))
        result=valor1+valor2
        print(result)
    elif(opcao == '-'):
        valor1 = float(input("Digite o primeiro valor"))
        valor2 = float(input("Digite o Segundo valor"))
        result = valor1 - valor2
        print(result)
    elif(opcao == '*'):
        valor1 = float(input("Digite o primeiro valor"))
        valor2 = float(input("Digite o Segundo valor"))
        result = valor1 * valor2
        print(result)
    elif(opcao == '/'):
        valor1 = float(input("Digite o primeiro valor"))
        valor2 = float(input("Digite o Segundo valor"))
        result = valor1 / valor2
        print(result)
    elif(opcao == '**'):
        valor1 = float(input("Digite o primeiro valor"))
        valor2 = float(input("Digite o Segundo valor"))
        result = valor1 ** valor2
        print(result)
    elif(opcao == 'r'):
        valor1 = float(input("Digite o primeiro valor"))
        result = valor1 **0.5
        print(result)
















