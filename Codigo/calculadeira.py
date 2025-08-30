continuar = "s"

while (continuar == "s"): 
    operacao = input("Qual operação deseja realizar? (+, -, *, /): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        print(num1 + num2)
    elif operacao == "-":
        print(num1 - num2)
    elif operacao == "*":
        print(num1 * num2)
    elif operacao == "/":
        print(num1 / num2)
    else:
        print("Operação inválida")
        
    continuar = input("Deseja realizar outra operação? (s/n): ")
    
    if continuar == "n":
        break

print("Obrigado(a) por utilizar nosso programa!")