def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "cannot divide by zero"
while True:
    num1=float(input("Enter the first number:"))
    operator=input("Enter operator(+,-,*,/):")
    num2=float(input("Enter the second number:")) 
    if operator=="+":
        result=add(num1,num2)
    elif operator=="-":
        result=subtract(num1,num2)

    elif operator=="*":
        result=multiply(num1,num2)
    elif operator=="/":
        result=divide(num1,num2)
    else:
        print("Invalid operator")
        continue
    print("Result:",result)
    another_cal=input("Do you want to perform another calculation? (yes/no):")
    if another_cal.lower()!="yes":
        break

