s=input()
s=list(s)
a=[0]*len(s)
for i in range(len(s)):
    if s[i].isalnum()==False:
        a[i]=s[i]
s=sorted(s)
l=[i for i in s if i.isalnum()==True]
j=0
for i in range(len(a)):
    if a[i]==0:
        a[i]=l[j]
        j+=1
s1=""
for i in a:
    s1+=i
print(s1)
