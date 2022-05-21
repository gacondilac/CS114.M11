from math import sqrt
import math

a=float(input())
b=float(input())
c=float(input())

def kiemtra(a,b,c):
    if(a+b>c)&(a+c>b)&(b+c>a):
        return 1
    else:
        return 0

def nhandang(a,b,c):
    p=(a+b+c)/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    s=round(s,2)
    if(s % 1 == 0):
        s = int(math.floor(s))
        s = round(s, 2 - int(math.floor(math.log10(abs(s)))))
    if(a==b)&(b==c):
        print("Tam giac deu, dien tich =",s)
    elif (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b):
        print("Tam giac vuong, dien tich =",s)
    elif (a==b) or (a==c) or (b==c):
        print("Tam giac can, dien tich ",s)
    
    else:
        print("Tam giac thuong, dien tich =",s)

if kiemtra(a,b,c)==1:
    nhandang(a,b,c)
else:
    print("Khong phai tam giac")