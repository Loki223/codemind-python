n=int(input())
c=1
s=0
for i in str(n):
    s+=int(i)**c
    c+=1
if n==s:
    print(True)
else:
    print(False)