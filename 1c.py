a=int(input("Ведите год: "))
if  (a%4==0 and a%10!=0) or a%400==0:
    print(a,"год високосный")
else:
    print( a ,"год НЕ високосный")
    print ("Ближайший високосный год ", a+(4-(a%4)), "будет через", 4-a%4, "года")
#добавила вычисление ближайшего високосного года
