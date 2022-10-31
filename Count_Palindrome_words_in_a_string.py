l=input().split()
c=0
for i in l:
    if i.lower() == i[::-1].lower():
        c+=1
print(c)