#marriage eligible
male=input("Are u Male(y/n)?")
age=int(input("Enter the age=>"))
if(male=="y" and male=="Y"):
    if(age>=21):
        print("U r eligible:")
    else:
        print("U r not eligible:")
else:
    if(age>=18):
         print("U r eligible:")
    else:
        print("U r not eligible:")
        
        
