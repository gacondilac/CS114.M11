def ucln(a,b):
    if(b==0):
        return a;
    return ucln(b,a%b);
n=int(input())
a=[]
for i in range(n):
    x,y=[int(a) for a in input().split()]
    UCLN=ucln(x,y)
    x=x//UCLN
    y=y//UCLN
    a.append((x,y))
for i in range(n):
    if a[i][1] != 1:
        print(int(a[i][0]), int(a[i][1]))
    else:
        print(int(a[i][0]))
