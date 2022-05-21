import math
q=int(input())
arr=[]
for i in range(q):
    n=int(input())
    a=[int(x) for x in input().split()]
    avg=sum(a)/len(a)
    avg=math.ceil(avg)
    arr.append(avg)
for i in range(q):
    print(arr[i])