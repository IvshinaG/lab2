a=int(input("Введите номер места:"))
if a>36 and a<55:
    if a%2==1:
        print("Ваше место боковое нижнее")
    else:
        print("Ваше место боковое верхнее") #добавила распределение на нижнее/вернее боковое место
elif a<37:
    if a%2==1:
        print("Ваше место нижнее купе")
    else:
        print("Ваше место верхнее купе ")
else:
    print("Места не существует")