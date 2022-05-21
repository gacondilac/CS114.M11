A = ""
dung =0
while dung==0:
    l = [i for i in input().split()]
    if l[0] == 0:
        A=l[1]+" "+A
    
    elif l[0] == 1:
        A+=" "+l[1]
    
    elif l[0] == 2:
        if l[1] in A:
             A=A.replace(l[1],l[2],1)
        else:
            A=l[1]+" "+A
    
    elif l[0] == 3:
        if l[1] in A:
            A=A.replace(l[1]+" ","",1)
    
    elif l[0] == 4:
        while l[1] in A:
            A=A.replace(l[1]+" ","")
    
    elif l[0] == 5:
        A=A[2:]
    elif l[0]==6:
        dung=1
if len(A)!=0:
    print(*A,sep=" ")
else:
    print("blank")