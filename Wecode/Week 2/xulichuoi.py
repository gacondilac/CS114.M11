s=input()
arr=[]
for i in range(len(s)):
    if s[i] not in "oiuyeaOIUYEA":
        arr.append(".")
        arr.append(s[i])
answer="".join(arr)
print(answer.lower())

