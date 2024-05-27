#Escriba un programa para que dado el número del mes, indique el número de días del mes
numero_mes = int(input("Ingresa el número del mes (1-12): "))

if numero_mes == 1 or numero_mes == 3 or numero_mes == 5 or numero_mes == 7 or numero_mes == 8 or numero_mes == 10 or numero_mes == 12:
    print("El mes", numero_mes, "tiene 31 días.")
elif numero_mes == 4 or numero_mes == 6 or numero_mes == 9 or numero_mes == 11:
    print("El mes", numero_mes, "tiene 30 días.")
elif numero_mes == 2:
    print("El mes 2 tiene 28 o 29 días (dependiendo del año).")
else:
    print("Número de mes inválido. ingresar un número entre 1 y 12.")











