# Crear una lista de 20 números enteros
lista_numeros = [int(input("Ingrese un número entero: ")) for _ in range(20)]

print("Lista de números:", lista_numeros)

numero_mayor = max(lista_numeros)
posicion_mayor = lista_numeros.index(numero_mayor)

print("El número mayor es:", numero_mayor)
print("La posición que ocupa dentro de la lista es:", posicion_mayor)