from math import sqrt
def fibonaci(n):
    # cach 1: time limit and runtime error test case 2 and 3 
   # if n==1 or n==2:
   #     return 1
   # else: 
   #     return fibonaci(n-1)+fibonaci(n-2)
   return (pow((1.0 + sqrt(5.0)), n) - pow((1.0 - sqrt(5.0)), n)) / (pow(2.0, n) * sqrt(5.0))

x=int(input())
if x<1 or x>30:
    print("So ",x," khong nam trong khoang [1,30].")
else:
    print(int(fibonaci(x)))