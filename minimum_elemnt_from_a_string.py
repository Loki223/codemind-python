s=input().split()
a=s[len(s)-1]
m=min(a)
if m and m.lower() in a:
    print(m.lower())
else:
    print(m)