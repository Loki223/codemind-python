a=int(input())
b=int(input())
pa=0
pb=0
for i in range(1,a):
    if a%i==0:
        pa+=i
for i in range(1,b):
    if b%i==0:
        pb+=i
if pa==b and pb==a:
    print("Amicable")
else:
    print("Not Amicable")