#Aplicar el IVA al precio de un producto. Alison Garcia Rosales.
precio = int (input("Digite el precio del producto C$: "))
cantidad = int (input("Digite la cantidad del producto: "))
total= cantidad * precio
totalFinal = total+((15/100)*total)
print ("Total a pagar mas 15% IVA: ",total,"C$, ", totalFinal, "C$", sep = "")