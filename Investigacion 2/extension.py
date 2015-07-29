
nom = input ("Favor Ingresar nombre de archivo con su extension: ")
archivo = open(nom,"r")
contenido = archivo.read()
print(contenido)