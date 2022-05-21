a,b = (int(x) for x in input().split())
#nhap mang voi so luong phan tu nhat dinh
arr_a = list(map(int,input().strip().split()))[:a]
arr_b = list(map(int,input().strip().split()))[:b]
arr_s=arr_a+arr_b
arr_s = sorted(arr_s)
#xuat mang ko co ngoac //ex:1 2 3 4
print(*arr_s[:],sep=' ')
