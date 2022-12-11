s1=input().lower().split()
s2=input().lower().split()
l=[i for i in s2 if i in s1 and s2.count(i)==1 and s1.count(i)==1]
print(len(l))