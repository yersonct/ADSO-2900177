#Ingresar el monton de tres persona que invirtieron para crear una empresa... pero a esta tres personas va a tener una ganascias diferente valor anual 
# la primera persona va a tener una ganancia del 30%
# la segunda persona va a tener una ganancia del 40%
# la tercera persona va a tener una ganancia del 30%
# Ppd
# Spd
# Tpd
# Mt  
Ppd = 0.3
Spd = 0.4
Tpd = 0.3
Mt = 0.0
while True:
    try:
        Mt = float(input("Señor usuario ingrese el montòn de dinero: "))
        Ppd = Mt*(1+Ppd)**1
        print("El montòn de la primera persona es: ",Ppd)
        Spd = Mt*(1+Spd)**1
        print("El montòn de la segunda persona es: ",Spd)
        Tpd = Mt*(1+Tpd)**1
        print("El montòn de la tercer persona es: ",Tpd)
        break
    except:
        print("Señor usuario no es un montòn de dinero, intente de nuevo")

