sub1=int(input("Enter sub1 marks:-"))
sub2=int(input("Enter sub2 marks:-"))
sub3=int(input("Enter sub3 marks:-"))
avg=(sub1+sub2+sub3)/3
if avg>=75:
    print("A+")
elif avg<75 and avg>=65:
    print("A")
elif avg<65 and avg>=55:
    print("B")
elif avg<55 and avg>=45:
    print("C")
elif avg<45 and avg>=35:
    print("D")
elif avg<35:
    print("Ordinary Pass")
