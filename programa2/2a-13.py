#Escriba un programa para ingresar todos los lados de un triángulo y verifique si es válido o no.

lado1 = float(input("Ingresa la longitud lado1: \n"))
lado2 = float(input("Ingresa la longitud lado2: \n"))
lado3 = float(input("Ingresa la longitud lado3: \n"))


if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Los lados ingresados forman un triángulo.")
else:
    print("Los lados ingresados no forman un triángulo válido.")