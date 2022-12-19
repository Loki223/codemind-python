def pall(n):
    n=str(n)
    if n==n[-1:-len(n)-1:-1]:
        return True
    else:
        return False
n=int(input())
print(pall(n))