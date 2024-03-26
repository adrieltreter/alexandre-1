print('programa dpara calcular imposto de renda.')
salario=float(input('digite o valor do salario'))
if(salario<= 1903.98):
    print('voce esta insento de imposto de renda')
elif(salario >1903.99 and salario <= 2826.65):
    imposto = (salario * 7.5)/100
    print('voce devera pagar r$ {} de imposto de renda'.format(imposto))
elif(salario >2826.66 and salario <= 3751.05):
    imposto = (salario * 15)/100
    print('voce devera pagar r$ {} de imposto de renda'.format(imposto))
elif (salario > 371.05 and salario <= 4664.68):
    imposto = (salario * 22.5)/ 100
    print('voce devera pagar r$ {} de imposto de renda'.format(imposto))
else:
    imposto = (salario * 27.5) /100
    print('voce devera pagar r$ {} de imposto de renda'.format(imposto))
