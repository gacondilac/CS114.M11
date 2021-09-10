x =int(input())
y=len(str(x))

s=0
k=x
while k>0:
    d=k%10
    s+=(d**y)
    k=k//10
if s == x:
    print(True)
else:
    print(False)
