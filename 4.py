a=int(input("введите курс валюты:"))
b=int(input("введите количество дней:"))
c=int(input("введите процент:"))
for i in range(b+1):
    print(a*(1+c/100)**i)