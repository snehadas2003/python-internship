print("1,addition")
print("2,subtraction")
print("3,muitiplication")
print("4,division")
print("5,exit")
a = int(input("enter the operation"))
if a==1:
    x=int(input("enter the 1st num"))
    y=int(input("enter the 2nd num"))
    sum=x+y
    print(sum)
elif a==2:
    x=int(input("enter the 1st num"))
    y=int(input("enter the 2nd num"))
    sub=x-y
    print(sub)
elif a==3:
    x=int(input("enter the 1st num"))
    y=int(input("enter the 2nd num"))
    mul=x*y
    print(mul)
elif a==4:
    x=int(input("enter the 1st num"))
    y=int(input("enter the 2nd num"))
    div=x/y
    print(div)
elif a>=5:
    print(exit)
    



