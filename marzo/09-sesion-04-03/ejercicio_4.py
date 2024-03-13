#Que ingrese un valor y elevarlo al cubo 
num = 0
while True:
    try:
        num = float(input("Señor usuario ingrese un numero: "))
        num = num * num * num
        print("Tu numero valor es: ",num)
        break
    except:
        print("señor usuario no es un numero")