s1=input().split()
s2=input().split()
for i in s2:
    for j in s1:
        if i.lower()==j.lower():
            print(i,end=" ")