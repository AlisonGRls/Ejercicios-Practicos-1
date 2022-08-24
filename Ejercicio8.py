#Leer x cantidad de precios y mostrar el precio mas alto y el precio más bajo. Alison Garcia
numeros = []
cant = int(input("¿Cuantos precios?: "))
for i in range(cant):
   lista = int(input(">> "))
   numeros.append(lista)

maximo = max(numeros)
minimo = min(numeros)

print ("El precio mas alto es: ", maximo, "C$ y el mas bajo: ", minimo, "C$", sep="")