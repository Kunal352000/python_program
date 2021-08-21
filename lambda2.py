num=int(input("Enter your number: "))
def check(x):
    if x>0:
        return "positive"
    elif x<0:
        return "negitive"
    else:
        return "zero"
print(check(num))

num1=int(input("Enter your number: "))
check1=(lambda x:"positive" if x>0 else "negative" if x<0 else "zero")
print(check1(num1))
