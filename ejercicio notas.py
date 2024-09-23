nota=float(input("Ingresa tu nota de 0 a 100 "))
while (nota<0)or(nota>100):
    print("error")
    nota= int(input("Ingresa tu nota de 0 a 100"))
if (nota>=90)and(nota<=100):
    print("su nota es A")
if (nota>=80)and(nota<=89):
    print("su nota es B")
if (nota>=70)and(nota<=79):
    print("su nota es C")
if (nota>=60)and(nota<=69):
    print("su nota es D")
if(nota>=0)and(nota<=59):
    print("su nota es F")
    