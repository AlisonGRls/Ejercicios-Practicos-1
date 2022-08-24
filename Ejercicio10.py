"""Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique
si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda
después del retiro. Alison Garcia"""
numCuenta = int(input("Ingrese el numero de cuenta:"))
saldo = int(input("Ingrese el saldo:"))
retiro = int(input("Ingrese el monto de retiro:"))

if retiro >= saldo:
   print("Lo sentioms, no realizar el retiro. El monto ha retirar excede su saldo.")
   print("saldo: ", saldo, "retiro:", retiro)
else:
   saldo = saldo - retiro
   print("numero de cuenta: ",numCuenta, sep="")
   print("Ha retirado ", retiro, "C$ de su cuenta de ahorro. Su saldo actual: ",saldo, sep="")