s=input().split()
v="AEIOUaeiou"
p=0
for i in s:
    m=len(i)-1
    for j in range(len(i)):
        if (i[j] in v and i[m] not in v) or (i[m] in v and i[j] not in v):
            p+=1
        m=m-1
print(p//2)