#Mostrar los tiempo recorrido durante tres dìas a la semana y ver su promedio
#l =lunes 
#M =Miercoles
#V =viernes
#T =Tiempo  
#P =Promedio

while True:
    try:
        print("Señor usuario ingrese los tiempo recorrido de cada dia")
        L = float(input("Lunes: "))
        M = float(input("Martes: "))
        V = float(input("Viernes: "))
        T = L+M+V
        P = T/3
        print("El tiempo del lunes fue: ",L)
        print("El tiempo del martes fue: ",M)
        print("El tiempo del viernes fue: ",V)
        print("la suma de los tres tiempos fue: ",T)
        print("El tiempo promedio fue: ",P)
        break
    except:     
        print("señor usuario no es un tiempo")