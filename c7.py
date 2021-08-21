#calculate the price based on discount
cp=float(input("Enter the cost price:"))
if(cp>=4000):
    dis=cp*(25/100)
else:
    dis=cp*(5/100)

sp=cp-dis
print("you get discount=>",dis)
print("you pay=>",sp)
