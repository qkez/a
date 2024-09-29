P=int(input("население"))
r=int(input("процентный прирост"))
n=int(input("количество лет"))

for i in range (n+1):
    print(P*(1+r/100)**i)