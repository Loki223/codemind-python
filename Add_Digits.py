def s(a):
    su=0
    for i in a:
        su+=int(i)
    return su
n=int(input())
while True:
    if s(list(str(n)))<=9:
        print(s(list(str(n))))
        break
    else:
        n=s(list(str(n)))