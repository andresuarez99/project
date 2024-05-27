#Calcular las soluciones x1, x2 de una ecuacíon de segundo grado dados loscoeficientes a, b, y c.
a=float(input("ingrese el valor de a \n"))
b=float(input("ingrese el valor de b \n"))
c=float(input("ingrese el valor de c \n"))
d= b**2 - 4*a*c
x1= (-b+d**(1/2))/(2*a)
x2= (-b-d**(1/2))/(2*a)
if d<0:
    print("la ecuacion no tiene solucion")
else:
    print("x1 es:", x1)
    print("x2 es:", x2)











