#Dada una lista de números hallar la mediana
numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_ordenados = numeros[:]
numeros_ordenados.sort()

n = 0
for _ in numeros_ordenados:
    n += 1
if n % 2 == 1:
       mediana = numeros_ordenados[n // 2]
else:
    mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2
print("La mediana de la lista es:", mediana)









