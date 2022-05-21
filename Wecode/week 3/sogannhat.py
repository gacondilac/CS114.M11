n=int(input())
arr=[int(x) for x in input().split()]
k,x=(int(x) for x in input().split())
start = 0
min_gap = x*k-sum(arr[0:k])

for i in range(k,n):
    new_gap=min_gap-abs(x-arr[start])+abs(x-arr[i])
    if new_gap<=min_gap:
        min_gap=new_gap
        start+=1
print(*arr[start: start+k],sep=' ')

