s=input()
c=0
for i in s:
    if 65<=ord(i)<=90 or  ord(i)==32 or 97<=ord(i)<=122 :
        c+=1
print(len(s)-c)