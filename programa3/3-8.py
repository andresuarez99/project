#Dada una lista de dígitos (o letras) determinar si es palíndromo
def es_palindromo(lista):
    lista_invertida = lista[::-1]
    if lista == lista_invertida:
        return True
    else:
        return False
lista = [1, 2, 3, 4, 3, 2, 1]
if es_palindromo(lista):
    print("La lista es un palíndromo.")
else:
    print("La lista no es un palíndromo.")












