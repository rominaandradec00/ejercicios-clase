unidad_origen=input("Ingresa la unidad de origen entre (Celsius/Fahrenheit/Kelvin)")
unidad_convertir=input("Ingresa la unidad a convertir entre(Celsius/Fahrenheit/Kelvin)")
temperatura_convertir=int(input("Ingresa el valor a convertir"))
while(unidad_origen=="Ingresa la unidad a convertir entre(Celsius/Fahrenheit/Kelvin"):
    print("error")
unidad_origen = input("Ingresa la unidad de origen entre (Celsius/Fahrenheit/Kelvin)")
unidad_convertir = input("Ingresa la unidad a convertir entre(Celsius/Fahrenheit/Kelvin)")
temperatura_convertir = int(input("Ingresa el valor a convertir"))
if (unidad_origen=="Celsius")and(unidad_convertir=="Kelvin"):
    temperatura_convertir=(temperatura_convertir+273)
    print("La temperatura en Kelvin es:",temperatura_convertir)
if(unidad_origen=="Kelvin")and(unidad_convertir=="Fahrenheit"):
    temperatura_convertir=((9/5*(temperatura_convertir-273))+32)
    print("La temperatura en Fahrenheit es:",temperatura_convertir)
if(unidad_origen=="Fahrenheit")and(unidad_convertir=="Celsius"):
    temperatura_convertir = (5/9*(temperatura_convertir+32))
    print("La temperatura en Celsius es:",temperatura_convertir)
if (unidad_origen == "Celsius") and (unidad_convertir!="Celsius"!="kelvin"):
    temperatura_convertir =((9/5*temperatura_convertir)+32)
    print("la temperatura en Fahrenheit es:", temperatura_convertir)
if(unidad_origen=="Fahrenheit")and(unidad_convertir!="Celsius"!="Fahrenheit"):
    temperatura_convertir = ((5/9*(temperatura_convertir-32))+273)
    print("la temperatura en Kelvin es:", temperatura_convertir)
else:
    if(unidad_origen!="Fahrenheit"!="Celsius")and(unidad_convertir=="Celsius"):
        temperatura_convertir=(temperatura_convertir-273)
        print("La temperatura en Celsius es:",temperatura_convertir)































