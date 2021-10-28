from random import*
m=0
print("Хочешь поиграть?")
while a.isalpha()!=True:
    a=int(input("Камень - 1, ножницы - 2, бумага - 3?"))
try:
    TypeError
b=randrange(1,3)
if b==1:
    print("Камень")
elif b==2:
    print("Ножницы")
elif b==3:
    print("Бумага")
if a>b:
    print("dsf")
elif a==b:
    print("ничья")
elif b>a:
    print("fff")