print("*********************************")
print("Bem Vindo no Jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = input("Digite o seu número: ")

print("Você Digitou", chute) #Para converter Str em Int

numero = int(chute)

if (numero_secreto == numero):
    print("Você acertou :)")
else:
    print("Você errou :(")

print("Fim de Jogo!")