def vowelc(s):
    c=0
    v="aeiouAEIOU"
    for i in s:
        if i in v:
            c+=1
    return c
s=input().split()
a=[vowelc(i) for i in s]
print(min(a))