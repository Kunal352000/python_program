#avg student
noStudent=int(input("Enter number student=>"))
for i in range(noStudent):
    mth=float(input("Enter marks of mth=>"))
    phy=float(input("Enter marks of phy=>"))
    che=float(input("Enter marks of che=>"))
    hin=float(input("Enter marks of hin=>"))
    eng=float(input("Enter marks of eng=>"))
    total=mth+phy+che+hin+eng
    per=total/5
    print("Percentage",per,"%")

avg=per/noStudent
print("Averge percentage=>",avg,"%")
