print("Programa que converte segundos em H:M:S.")
total_segundos = int(input("Informe o número total de segundos:"))
minutos = total_segundos // 60
segundos = total_segundos%60
horas=minutos // 60
minutos = minutos% 60
print(horas, ":", minutos,":", segundos)