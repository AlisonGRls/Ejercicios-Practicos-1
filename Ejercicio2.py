"""Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
estudiante de manera individual, escriba un código en Python que permita crear un correo
electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
“@est.uca.edu.ni”. Alison Garcia."""
p_info = []
print ("Ingrese sus nombres y apellidos: ")
for i in range(4):
   info = str(input(">>: "))
   p_info.append(info)

print("Su nuevo correo institucional: ", *p_info)

for i in range(len(p_info)):
    p_info[i] = p_info[i].lower()

print(p_info[0], ".", p_info[2], "@est.uca.edu.ni", sep = "")