s=input()
s=s.lower()
s=set(s)
d=[]
for i in s:
    if i!=" ":
        d.append(i)
print(len(d))