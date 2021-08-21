#passenger ticket
num=int(input("Enter number of passengers=>"))
total=0
for i in range(num):
    age=int(input("Enter age:"))
    ticket=int(input("Enter price:"))
    if(age<=12):
        total=ticket-(ticket*30)/100
        print("Plz pay=>",total)
    elif(age>=59):
        total=ticket-(ticket*50)/100
        print("Plz pay=>",total)
    else:
        print("Plz pay=>",ticket)
        
