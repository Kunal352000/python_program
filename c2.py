#selling price,cost price student discount
ans=input("Are you a student(y/n)?")
cp=float(input("Enter the amount of purchase:"))
if(ans=="y" or ans=="Y"):
    if(cp>=2000):
        dis=(cp*40)/100
    else:
        dis=(cp*20)/100
else:
    if(cp>=4000):
        dis=(cp*30)/100
    else:
        dis=(cp*5)/100

sp=cp-dis
print("Please pay",sp)
