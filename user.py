a=(input("enter the username"))
x=a.isalnum()
print(x)
if len(a)>15:
   print("length exceeded")
if len(a)<6:
    print("length too short")
if x==True:
    print("validated")
else:
    print("it can't be validated")


