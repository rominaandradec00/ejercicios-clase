estado_civil=input("Ingresa tu estado civil [soltero/casado]")
sueldo=float(input("Ingresa tu sueldo"))
if(estado_civil=="Soltero"):
    if(sueldo<=30000):
        TI=0.10
    if (sueldo>30000)and(sueldo>=70000):
        TI=0.20
    if (sueldo>70000):
        TI=0.30
else:
    if (sueldo<=40000):
        TI=0.08
    if (sueldo>40000)and(sueldo<=90000):
        TI=0.15
    if (sueldo>90000):
        TI=0.25
    IMPUESTO=sueldo*TI
    print("El impuesto calculado a pagar es:     ",IMPUESTO)

