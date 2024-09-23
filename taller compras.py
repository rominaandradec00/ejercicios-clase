n=int(input("Ingrese la cantidad de productos por comprar:   "))
c=1
total=0
while (c <= n):
    precio=float(input("Ingrese el precio del producto:    "))
    total=(total+precio)
    c=c+1
print(f"el total a pagar es:  ${total}")
if(n>=1)and(n<=4):
  print("sin descuento")
  DESC=0.0
  if(total>1000):
     print ("Se aplica un 5% de descuento adicional,por compras mayor a $1000")
     DESC=DESC+0.95
     NUEVO_TOTAL=total*DESC
     print("El nuevo total a pagar es:   $",NUEVO_TOTAL)
else:
   if(n>=5)and(n<=9):
        print("Se aplica 10% de descuento")
        DESC=0.90
   if(n>=10)and(n<=19):
        print("Se aplica 15% de descuento")
        DESC=0.85
   if(n>=20):
        print("Se aplica 20% de descuento")
        DESC=0.70
   if(total>1000):
      print ("Se aplica un 5% de descuento adicional,por compras mayor a $1000")
      DESC=DESC-0.05
      NUEVO_TOTAL=total*DESC
      print("El nuevo total a pagar es:   $",NUEVO_TOTAL)
