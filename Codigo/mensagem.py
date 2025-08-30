continuar = "s"
while continuar == "s":
    n = int(input('Quantas vezes deseja exibir a mensagem?\n '))

    for i in range(n):
        print("Hello World")
        
    continuar = input("Deseja continuar? (s/n)")

print("Obrigado(a) por utilizar nosso programa. Volte sempre! ;)")