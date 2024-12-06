h=float(input("enter the height:"))
w=float(input("enter the weight:"))
def bmi(h,w):
    bmi=w/(h**2)
    return bmi
result=(bmi(h,w))
print(result)