num=int(input("Enter your number: "))
def pnz(x):
    if x>0:
        print("positive")
    elif x==0:
        print("zero")
    else:
        print("negative")
pnz(num)

num1=int(input("Enter your number1: "))
pnz1=lambda x:"positive" if x>0 else "negative" if x<0 else "zero"
print(pnz1)
