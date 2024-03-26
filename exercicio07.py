print("programa de tabuada.")

numero = int(input("entre com um numero inteiro:"))
contador = 1
while(contador <= 10):
    resultado = numero * contador
    print(numero, "x",contador, "=", resultado)
    contador = contador + 1