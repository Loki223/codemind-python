n=int(input())
n=str(n)
s=""
for i in n[-1:-len(n)-1:-1]:
    s+=i
print(s)