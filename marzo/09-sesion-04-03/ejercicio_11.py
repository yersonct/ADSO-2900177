#hacer el total de pulsaciones por segundo 
#P = pulsaciones
#Edad = Edad de la persona 

while True:
    try:
        Edad = int(input("indique la edad desde 1 hasta 120: "))
        if Edad<1 or Edad>120:
            print("señor usuario tu edad no esta en el rango del 1 al 120 ")
        else:
            P = (220-Edad)/10
            print("las pulsaciones que tiene que tener un persona, por cada 10 segundo es: ",P)
        break
    except:
        print("No es una pulsacion")