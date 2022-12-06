s=input().split()
smin=smax=0
for i in s:
    smin+=ord(min(i))
    smax+=ord(max(i))
print(smax-smin)