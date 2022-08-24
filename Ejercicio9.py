"""Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio.
Evaluar si apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85
en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a
95. Alison Garcia"""
nombre = input("Nombre: ")
apellidos = input ("Apellidos: ")
promedio = int(input ("promedio: "))

def validacion (promedio):
   if promedio >= 85:
      print ("¡", nombre, apellidos,"Puesdes optar a la beca!")
   else:
      print ("Lo siento", nombre, apellidos,", No puedes optar por la beca")

print("Menú--Carreras--")
print(" 1. Lic. psicologia\n 2. lic. Teologia\n 3.ing. Industrial\n 4. ing. Electrica\n 5. ing. Sistemas")
op = int(input(">> "))
if op == 1:
   validacion(promedio)
elif op == 2:
   validacion(promedio)
elif op == 3:
   validacion(promedio)
elif op == 4:
   validacion(promedio)
elif op == 5:
   if promedio >= 95:
      print ("¡", nombre, apellidos,"Puesdes optar a la beca!")
   else:
      print ("Lo siento", nombre, apellidos,", No puedes optar por la beca")
else:
   print("Opcion no valida")