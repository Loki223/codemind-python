s=input()
v="AEIOUaeiou"
p=0
m=len(s)-1
for i in range(len(s)//2):
    if s[i]!=" " or s[m]!=" ":
        if ((s[i] in v and (s[m] not in v and s[m]!=" ")) or (s[m] in v and (s[i] not in v and s[i]!=" ")) ):
            p+=1
    m-=1
print(p)