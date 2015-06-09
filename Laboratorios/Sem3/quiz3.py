nom = input ("ingrese el nombre: ")

venta1= input ("ingrese venta 1: ")
venta2= input ("ingrese venta 2: ")
venta3= input ("ingrese venta 3: ")

ventas = int(venta1) + int(venta2) + int(venta3) 

comision= float (ventas)*0.125 

print ("Vendedor\tVentas\tComision\n------\t\t------\t------\n"+nom+"\t\t"+str(ventas)+"\t"+str(comision))
