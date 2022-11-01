s=input()
c=[]
for i in s:
    if i not in c:
        c.append(i)
if len(c)==len(s):
    print(True)
else:
    print(False)