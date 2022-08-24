#Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números
#enteros. Alison Garcia.
numeros = []
cant = int(input("¿Cuantos numeros?: "))
for i in range(cant):
   lista = int(input(">>: "))
   numeros.append(lista)
print("Numeros pares:")
for lista in numeros:
   if lista % 2 == 0:
      print (lista, end = " ")