# Que el usuario ingrese el numero y que se implima 
num = 0
while True:
    try:
        num =float(input("señor usuario ingrese un cualquier valor: "))
        print("señor usuario tu valor es: ",num)
        break
    # vamos hacer que el usuario solo ingrese numero no letras
    except:
        print("señor usuario el valor que ingreso no es un numero")
        print("ingrese nuevamente un numero")