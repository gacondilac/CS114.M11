h,w = (int(x) for x in input().split())
matrix=[]
for i in range(h):
    arr_a = list(map(int,input().strip().split()))[:w]
    matrix.append(arr_a)
t,l,b,r = (int(x) for x in input().split())
for i in range(h):
    for j in range(w):
        print(matrix[i][j], end = " ")
    print()