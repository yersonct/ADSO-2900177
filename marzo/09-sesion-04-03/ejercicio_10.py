#Pasar a grados kelvin a fahrenheit
while True:
    try:
        k=float(input("Señor usuario ingrese su grado kelvin: "))
        k = (9*(k-273.15)/5)+32
        print("Señor usuario tu temperatura fahrenheit es: ",k)
       
        break
    except:
        print("No es un  grado")