#Leer x cantidad de edades y mostrar el promedio de dichas edades. Alison Garcia.
edades = []
cant = int(input("Cuantas edades?: "))
for i in range(cant):
   edad = int(input("Dime tu edad: "))
   edades.append(edad)

promedio = sum(edades)/len(edades)
print("El promedio de edad es:", promedio)