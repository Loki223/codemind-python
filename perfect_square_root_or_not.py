import math
n=int(input())
s=math.sqrt(n)
if math.ceil(s)==math.floor(s):
    print(True)
else:
    print(False)