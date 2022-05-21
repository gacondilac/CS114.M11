n=int(input())
result=[0 for i in range(n)]
for i in range(n):
    p=input()
    q=input()
    arr=[0 for i in range(27)]
    check=0
    for j in range(len(p)):
        arr[ord(p[j])-97]=1
    for j in range(len(q)):
        if(arr[ord(q[j])-97]==1):
            check=1
            break
    result[i]=check
for i in range(n):
    if(result[i]==1):
        print("YES")
    else:
        print("NO")
