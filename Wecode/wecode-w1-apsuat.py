import math

a=float(input())
answer =a/(2.54**2/0.453592)
answer=round(answer,5-int(math.floor(math.log10(abs(answer)))))
print(answer)