
cont=0


print ("1.\tImprimir Numeros")
print ("2.\tAgregar Numeros")
print ("3.\tEliminar numeros")
print ("4.\tBuscar numeros de telefono")
print ("5.\tSalir")


Directorio={}

while cont<5:
	cont=int (input("Ingrese una opcion entre 1 y 5\n"))
	if cont==1:
		print (Directorio)
	elif cont==2:
		nom=input("Ingresar nombre\n")
		num=input("Ingresar telefono\n")
		Directorio[nom] = num
	elif cont==3:
		elim= input ("Ingresa nombre\n")
		del Directorio [elim]
	elif cont==4:
		elim= input ("Ingresar nombre\n")
		print (Directorio [elim])
    
