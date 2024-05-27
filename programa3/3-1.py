#Dada una lista de números encontrar el número mayor
numeros = [1, 5, 7, 9, 11, 13, 15, 18]

maximo = numeros[0]
for numero in numeros[1:]:
    if numero > maximo:
        maximo = numero
print("El número máximo en la lista es:", maximo)










