s=input().split()
for i in s:
    a=[0]*len(i)
    for j in range(len(i)):
        if i[j].isalnum()==False:
            a[j]=i[j]
    l=[j for j in i if j.isalnum()==True]
    l.sort()
    k=0
    for j in range(len(a)):
        if a[j]==0:
            a[j]=l[k]
            k+=1
    s1=""
    for j in a:
        s1+=j
    print(s1,end=" ")
            
            