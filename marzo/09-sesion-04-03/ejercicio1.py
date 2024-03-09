# Que el usuario ingrese un caracter y implimir su contenido
a = ""
a = input("señor usuario ingrese un caracter: ")
# reitero que tambien puede ser un numero un  caracter... pero por esta ocaciòn quiero que sea una letra

if a == "0" or a=="1"or a=="2" or a=="3" or a=="4" or a=="5" or a=="6" or a=="7" or a=="8" or a=="9":
    print("no es una cualidad suya señor usuario")
else:
    print("señor usuario tu caracter fue: ",a)