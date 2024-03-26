print("Programa que classifica triãngulo.")
a = float(input("Digite o primerio lado do triângulo"))
b = float(input("Digite o segundo lado do triãngulo"))
c = float(input("Digite o terceiro lado do triângulo"))

if(a > b+c) or (b > a+c) or (c > a+b):
    print("Não é um triângulo.")
else:
    print("É um triângulo.")

if(a == b and b == c):
    print("Triângulo equilátero.")
elif(a == b) or (b == c) or (a == c):
    print("Triângulo isóceles.")
else:
    print("Triângulo escaleno.")
