m,n=map(int,input().split())
i=1
if n%m==0 or m%n==0:
    if n<m:
        print(m)
    else:
        print(n)
else:
    while True:
        if n>m:
            a=m*i
            if a%n==0:
                print(a)
                break
            i+=1
        else:
            a=n*i
            if a%m==0:
                print(a)
                break
            i+=1