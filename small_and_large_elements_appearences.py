s=input()
a=[ord(i) for i in s if i!=" "]
print(chr(min(a)),a.count(min(a)),chr(max(a)),a.count(max(a)))
