q=int(input())
a=[]
for i in range(q):
    n=int(input())
    if n%2==0 and n!=2:
        a.append(0)
    elif n==2:
        a.append(2)
    elif n%2!=0 and n!=1:
        a.append(1)
    elif n==1:
        a.append(3)
for i in range(q):
    print(a[i])


