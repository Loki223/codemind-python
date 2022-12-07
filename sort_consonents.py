s=input().split()
v="AEIOUaeiou"
for i in s:
    a=[0]*len(i)
    for j in range(len(a)):
        if i[j] in v:
            #print(i[j])
            a[j]=i[j]
    sl=[j for j in i if j not in v]
    sl=sorted(sl)
    k=0
    l=0
    for j in a:
        if j==0:
            a[k]=sl[l]
            l+=1
        k+=1
    s1=""
    for k in a:
        s1+=k
    print(s1,end=" ")
                
    #print(s1,end=" ")
    