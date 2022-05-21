import math
F=float(input())

C = (F-32)/1.8
C=round(C,5-int(math.floor(math.log10(abs(C)))))
if(C % 1 == 0):
        C = int(math.floor(C))
        C = round(C, 2 - int(math.floor(math.log10(abs(C)))))
K= C + 273.15
K=round(K,5-int(math.floor(math.log10(abs(K)))))
if(K % 1 == 0):
        K = int(math.floor(K))
        K = round(K, 2 - int(math.floor(math.log10(abs(K)))))
print(C,K)