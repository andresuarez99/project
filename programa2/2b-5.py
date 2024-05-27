#Escriba un programa para hacer un patrón como un triángulo rectángulo con un número que repetirá un número seguido.
#El patrón como:
#1
#22
#333
#4444
num_filas = int(input("Ingresa el número de filas del triángulo: "))

for i in range(1, num_filas + 1):  
    for j in range(1, i + 1):
        print(i, end="")
    print() 








