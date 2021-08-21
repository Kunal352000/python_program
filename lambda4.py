s=lambda x,y: x if x>y else y
print("The biggest of {} and {}".format(10,20,s(10,20)))
print("The biggest of {} and {}".format(100,20,s(100,20)))
print("The biggest of {} and {}".format(10,-20,s(10,-20)))
print("The biggest of {} and {}".format(1000,2000.23,s(1000,2000.23)))
