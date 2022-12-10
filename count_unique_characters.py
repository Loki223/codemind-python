s=input()
s=s.lower()
a=[]
for i in s:
    c=0
    for j in s:
        if i.isalnum()==True and j.isalnum()==True:
            if i==j:
                c+=1
    if c==1:
        a.append(i)
print(len(a))