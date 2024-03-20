print("programa que classifica triangulo.")
a =float(input("digite o primeiro lado do triangulo"))
b =float(input("digite o segundo lado do triangulo"))
c =float(input("digite o terceiro lado do triangulo"))

if(a > b+c) or (b> a + c) or (c> a+b):
    print("nao é triangulo")
else:
    print("é um triangulo.")
    