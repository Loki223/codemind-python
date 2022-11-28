a=input()
b=input()
k=0
v=["a","e","i","o","u","A","E","I","O","U"]
for i in a:
    if i == b :
        print(True)
        print(k)
        break
    k+=1
else:
    print(False)