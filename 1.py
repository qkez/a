a = int(input("введите число"))
for i in range (100,a+1):
    n6=i%1000000//100000
    n5=i%100000//10000
    n4=i%10000//1000
    n3=i%1000//100
    n2=i%100//10
    n1=i%10
    if 100 > a > 1000000:
        pass

    if n4==0 and n5==0 and n6==0 and n3==n1:
        print(i)
    elif n5==0 and n6==0 and n4!=0 and n2==n3 and n4==n1:
        print(i)
    elif n6==0 and n5!=0 and n5==n1 and n4==n2:
        print(i)
    elif n6!=0 and n6==n1 and n5==n2 and n4==n3:
        print(i)
    else:
        pass
