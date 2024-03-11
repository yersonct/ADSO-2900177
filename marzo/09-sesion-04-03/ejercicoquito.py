#Que el usuario ingrese un valor y que ese valor se multiplique por 2 y otro que sea elevando a la 2 en esos dos valores diferente sumarle y mostrarlos
num1 = 0
num2 = 0
num3 = 0
while True:
    try:
        num1 = float(input("Señor usuario ingrese un numero: "))
        num2 = num1 * num1 
        num1 = num1*2
        num3 = num1 + num2
        print("El nuevo valor es: ",num3)
        break
    except:
        print("señor usuario no es un numero")