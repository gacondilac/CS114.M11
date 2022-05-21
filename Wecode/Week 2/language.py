s = input()
b=s.split()
num=len(b)
temp=0
P=["lios","liala","etr","etra","initis","inites"]
for i in P:
    for j in P:
        if i in j:
            temp+=1
if temp==num:
    print("YES")
else:
    print("NO")
