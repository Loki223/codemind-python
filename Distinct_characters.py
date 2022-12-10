s=input()
s=s.lower()
s=set(s)
d=[]
for i in s:
    if i!=" ":
        d.append(i)
s1=""
for i in sorted(d):
    s1+=i
print(s1)