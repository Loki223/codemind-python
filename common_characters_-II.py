s1=input().lower()
s2=input().lower()
k1=set(s1)
k2=set(s2)
l1=[i for i in k1 if i!=" "]
l2=[i for i in k2 if i!=" "]
a=[]
for i in l1:
    if i in l2:
        a.append(i)
for i in l2:
    if i in l1:
        a.append(i)
s1=""
for i in sorted(a):
    if i not in s1:
        s1+=i
print(len(s1))
