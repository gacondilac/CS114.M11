import math
x ,y  = [int(x) for x in input().split()]
ga=2*x-y/2
#if(ga % 1 == 0):
  #      ga = int(math.floor(ga))
   #     ga = round(ga, 2 - int(math.floor(math.log10(abs(ga)))))
cho=x-ga
#if(cho % 1 == 0):
    #    cho = int(math.floor(cho))
     #   cho = round(cho, 2 - int(math.floor(math.log10(abs(cho)))))
print(round(ga),round(cho))