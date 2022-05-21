k ,t  = [int(x) for x in input().split()]
round=t//k
point=t%k
if round % 2 ==0:
    print(point)
else:
    point=abs(k-point)
    print(point)