import sys


S = input().strip()
try:
    s1=int(S)
    print(s1)
except ValueError:
    print("BadString")
    
