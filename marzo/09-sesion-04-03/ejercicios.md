*1.Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.*

```
INICIO
  Definir dinero1,dinero2,dinero3,resul1,resul2,resul3,resul4 como real 
     dinero1<- 0.0
     dinero2<- 0.0
     dinero3<- 0.0
     resul1<- 0.0 
     resul2<-0.0 
     resul3<-0.0
  Escribir "señor usuario ingrese su cantidad de dinero de cada uno"
     Leer dinero1
     Leer dinero2
     Leer dinero3
     resul1<- dinero1+dinero2+dinero3
     resul2<- dinero1*100/resul1
     resul3<- dinero2*100/resul1
     resul4<- dinero3*100/resul1
  Escribiir "señor usuario la cantidad total de dinero es: ",resul1
  Escribir " señores usuario el porcentaje del primer usuario es: ",resul1," del segundo usuario es: ",resul2," y el ultimo tiene un porcentaje de: ",resul3
FIN
```

*2. Un alumno desea saber cuál será su promedio general en las tres materias más difíciles que cursa y cuál será el promedio que obtendrá en cada una de ellas. Estas materias se evalúan como se muestra a continuación:*

*La calificación de Matemáticas se obtiene de la siguiente manera: Examen 90% Promedio de tareas 10% En esta materia se pidió un total de tres tareas.*

*La calificación de Física se obtiene de la siguiente manera: Examen 80% Promedio de tareas 20% En esta materia se pidió un total de dos tareas.*

*La calificación de Química se obtiene de la siguiente manera: Examen 85% Promedio de tareas 15% En esta materia se pidió un promedio de tres tareas.*

```
INICIO
  Definir mt1,mt2,mt3,ft1,ft2,ft3,qt1,qt2,qt3 como real 
  Definir mate,fisi,quimi como real
  Definir resul1,resul2,resul3 como real 
  Definir exa1,exa2,exa3 como real 
    mate,fisi,quimi <- 5.0
    mt1,mt2,mt3,ft1,ft2,ft3,qt1,qt2,qt3 <- 0.0
    resul1,resul2,resul3 <-0.0
    exa1,exa2,exa3 <- 0.0
  Escribir "señor usuario ingrese la calificacion del examen de mate"
  leer exa1    
  Escribir "señor usuario ingrese la calificacion del examen de fisi"
  leer exa2    
  Escribir "señor usuario ingrese la calificacion del examen de quimi"
  leer exa3
    exa1<-exa1*0.9/mate
    exa2<-exa2*0.8/fisi
    exa3<-exa3*0.85/quimi
  Escribir "señor usuario ingrese la tres calificaciones de las tareas de mate"
  leer mt1
  leer mt2
  leer mt3
  Escribir "señor usuario ingrese la tres calificaciones de las tareas de fisi"
  leer ft1
  leer ft2
  leer ft3
  Escribir "señor usuario ingrese la tres calificaciones de las tareas de quimi"
  leer qt1
  leer qt2
  leer qt3
     resul1 <- mt1+mt2+mt3/3
     resul2 <- ft1+ft2+ft3/3
     resul3 <- qt1+qt2+qt3/3
     resul1<-resul1*0.1/mate
     resul2<-resul2*0.2/fisi
     resul3<-resul3*0.15/quimi
     mate <-(resul1+exa1)*mate
     fisi <-(resul1+exa1)*fisi
     quimi <-(resul1+exa1)*quimi
  Escribir "señor usuario la nota final de mate es: ",mate
  Escribir "señor usuario la nota final de mate es: ",fisi
  Escribir "señor usuario la nota final de mate es: ",quimi
FIN
```
* 3.Leer un real e imprimir si el número es positivo o negativo. *
```
INICIO
  Definir num como real 
    num <-0.0
  Escribir "señor usuario ingrese un numero: "
  Leer num
  si num > 0 entonces
    Escribir "señor usuario tu numero es positivo"
  sino 
    Escribir "señor usuario tu numero es negativo"

FIN
```
* 4.Leer un real e imprimir si el número es mayor a 200 o no.*
```
INICIO
  Definri num como real 
    num <- 0.0
  Escribir "señor usuario ingrese tu numero: "
    Leer num
  si num>200 entonces 
    Escribir "señor usuario tu numero es mayor que 200"
  sino 
    Escribir "señor usuario tu numero es menor que 200"
FIN
```
* 5.Leer un real e imprimir si el número está en el rango de 50 y 100. *
```
INICIO
  Definir num como real
   num <-0.0
  Escribir "señor usuario ingrese tu numero: "
   Leer num
  si num>=50 && num=<100 entonces
    Escribir "señor usuario tu numero esta en el rango"
  sino
    Escribir "señor usuario tu numero no esta en el rango 
FIN

```
