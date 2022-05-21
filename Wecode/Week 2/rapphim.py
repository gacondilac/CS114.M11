m,n,a=[int(x) for x in input().split()]
if m%a==0:
    x=m//a
else:
    x=x=m//a+1
if n%a==0:
    y=n//a
else:
    y=n//a+1
num=x*y
print(num)