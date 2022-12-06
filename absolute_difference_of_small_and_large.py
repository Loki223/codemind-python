s=input().split()
for i in s:
    d=ord(max(i))-ord(min(i))
    print(d,end=" ")