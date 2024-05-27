#Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número.
#El patrón como:
#1
#12
#123
#1234
num_filas = int(input("Ingresa el número de filas del triángulo: "))
for i in range(1, num_filas + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()












