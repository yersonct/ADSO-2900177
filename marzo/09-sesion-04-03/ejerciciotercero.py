#Elevar un numero al cuadrado
num = 0
while True:
    try:
        num = float(input("Señor usuario ingrese un numero: "))
        num = num * num
        print("Tu numero valor es: ",num)
        break
    except:
        print("señor usuario no es un numero")