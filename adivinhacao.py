import random

print("*********************")
print("bem vindo ao jogo de divinhação")
print("*********************")
numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
rodada = 1
pontos = 1000

print("Qual o nivel de dificuldade?")
print("(1) Facil - (2) Medio - (3) Dificil")
nivel = int(input("Defina o nivel:"))
if(nivel ==1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
  print("Tentativa {} de {}" .format( rodada, total_de_tentativas))
  chute = int(input("digite um número,"))

  if(chute < 1 or chute > 100):
    print("Digite um número entre 1 e 100")
    continue
  acertou=numero_secreto == chute
  maior=numero_secreto > chute
  menor=numero_secreto < chute
  print("você digitou: ",chute)
  if(acertou):
    print("você acertou e fez {} pontos." .format(pontos))
    break
  else:
    if (maior):
      print("voce errou: 0 número digitado é menor que o número secreto. Seus pontos",pontos)
    elif (menor):
        print("voce errou: 0 numero digitado é maior que o numero secreto. Seus pontos:",pontos)
        pontos_perdidos = abs( numero_secreto - chute )
        pontos = pontos - pontos_perdidos

print("O número secreto é:", numero_secreto)
print("fim de jogo.Seus pontos:",pontos)