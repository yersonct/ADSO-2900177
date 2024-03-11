#pasar grados kelvin a celsius
while True:
    try:
        k=float(input("Señor usuario ingrese su grado kelvin: "))
        k= k -273.15
        print("Señor usuario tu temperatura celsius es: ",k)
       
        break
    except:
        print("No es un  grado")