s1=input()
s2=input()
su1=su2=0
st1=s1.lower()
st2=s2.lower()
for i in st1:
    su1+=ord(i)
for j in st2:
    su2+=ord(j)
if su1==su2:
    print(True)
else:
    print(False)