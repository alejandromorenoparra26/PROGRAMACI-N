estacion = (input("¿En que estacion estamos? (invierno/verano):"))
temperatura = int(input("¿Que temperatura hace?"))

if estacion == "invierno" and temperatura < 20 :
    print( "encender: la calefaccion")
elif estacion == "verano" and temperatura > 25:
    print("encender el aire acondicionado")
else: 
    print("no es necesario encender ningun sistema de climatizacion")