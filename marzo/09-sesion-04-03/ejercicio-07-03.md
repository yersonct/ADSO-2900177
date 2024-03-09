### haga  que los usuarios ingresen 3 valores y que diga cual es: el mayor, el mediano y el menor. De lo contrario si los valores son iguales diga que hay digitos que son identicos.

* solution  *
```
Inicio
 while True:
    try:
        num1=float(input("señor usuario ingrese ingrese el primer valor: "))
        num2=float(input("señor usuario ingrese ingrese el segundo valor: "))
        num3=float(input("señor usuario ingrese ingrese el tercer valor: "))
        if num2 == num3 or num2 == num1  or num1 == num2 or num1 == num3 or num3 == num2 or num3 == num1:
            print("señor usuario, hay dos o mas digitos que son iguales😢")
            break
        else:
            if num1> num2:
                if num1>num3:
                    print("mayor: ",num1) 
                    if num3>num2:
                        print("medio: ",num3)
                        print("bajo: ",num2)
                    else :
                        print("medio: ",num2)   
                        print("bajo: ",num3)        
                else:
                    
                    if num3>num1:
                        if num3>num2:
                            print("mayor: ",num3)
                            print("medio: ",num1)
                            print("bajo: ",num2)
            else:
                if num2> num1:
                    if num2> num3:
                        print("mayor: ",num2)
                        if num3> num1:
                            print("medio: ",num3)
                            print("bajo: ",num1)
                        else:
                            print("medio: ",num1)    
                            print("bajo: ",num3)    
                    else:
                        if num3 > num2:
                            print("mayor: ",num3)
                            print("medio: ",num2)
                            print("bajo: ",num1)
    except:
        print("señor usuario no es un numero")
fin
```
