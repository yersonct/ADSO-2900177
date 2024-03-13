# hacer una tienda,Que los productos tenga un descuento de 0.08 "por cada uno", que el usuario ingrese la cantidad,el nombre del producto y el precio del producto
# Cp = Cantidad del producto 
# Np = Nombre del producto 
# Pp = Precio del producto 
# Vu = Valor unitNprio
# Vc = Valor con la cantidad
# Vd = valor con descuento 
# Vcd = valor con descuento 

Np = ""
Cp = 0.0
Pp = 0.0
Vu = 0.0
Vc = 0.0
Vd = 0.0
Vcd = 0.0

while True:
    try:
        Np = input("señor usuario ingrese el nombre del producto: ")
        if Np == "0" or Np =="1"or Np =="2" or Np =="3" or Np =="4" or Np =="5" or Np =="6" or Np =="7" or Np =="8" or Np =="9":
            print("Ningun producto esta registrado con este nombre: ",Np)
        else:
            try:
                Cp = int(input("Señor usuario ingrese la cantidad del producto: "))
                Pp = float(input("señor usuario ingrese el precio del producto: "))
                Vu = Pp
                Vc = Pp * Cp
                Vd = Vc * (0.08*Cp)
                Vcd = Vc -Vd
                print("señor usuario el valor unitario de tu producto es: ",Vu)
                print("señor usuario el valor total fue: ",Vc)
                print("señor usuario el descuento es: ",Vd)
                print("El valor con descuento: ",Vcd)
                break   
            except:  
                print("señor usuario no es un numero")  
    except:
        print("señor usuario no es el nombre del producto")