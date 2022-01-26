import random

print("*********************************")
print("Bem Vindo no Jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

print(numero_secreto)

for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")

    print("Você Digitou", chute_str) #Para converter Str em Int

    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou :)")
        break
    else:
        if(maior):
            print("Você errou :( O seu número foi maior que o número secreto.")
        elif (menor):
            print("Você errou :( O seu número foi menor que o número secreto.")

print("Fim de Jogo!")