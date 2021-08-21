n=int(input("Enter any number:"))
if(n%2!=0):
    print("Weird")
elif(n%2==0 and (n==2 or n<5)):
    print("Not Weird")
elif(n%2==0 and (n==6 or n<=20)):
        print("Weird")
elif(n%2==0 and n>20):
    print("Not weird")

