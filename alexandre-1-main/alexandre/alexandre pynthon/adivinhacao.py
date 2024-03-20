import random

print("*********************")
print("bem vindo ao jogo de divinhação")
print("*********************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3
rodada = 1
for rodada in range(1, total_de_tentativas + 1):
  print("Tentativa {} de {}" .format( rodada, total_de_tentativas))
  chute = int(input("digite um número,"))

  if(chute < 1 or chute > 100):
    print("Digite um número entre 1 e 100")

  acertou=numero_secreto == chute
  maior=numero_secreto > chute
  menor=numero_secreto < chute
  print("você digitou: ",chute)
  if(acertou):
    print("você acertou.")
    break
  else:
    if (maior):
      print("voce errou: 0 número digitado é menor que o número secreto")
    if (menor):
        print("voce errou: 0 numero digitado é maior que o numero secreto")
print("O número secreto é:", numero_secreto)
print("fim de jogo.")