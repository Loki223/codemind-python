n=int(input())
n=list(str(n))
while True:
    for i in range(len(n)):
        if n[i]=="6":
            n[i]="9"
            break
    break
for i in n:
    print(i,end="")