n=int(input())
k=int(input())
p=int(input())
q=int(input())

mark=(p-1)*2+q  
previous=mark-k
after=mark+k
if previous <=0:
    if after>=n:
        print(-1)
    else:
        if after%2==0:
            u=after/2
            v=2
            print(round(u),v)
        else:
            u=(after/2)+1
            v=1
            print(round(u),v)
else:
    if after >= n:
        if previous%2==0:
            u=previous/2
            v=2
            print(round(u),v)
        else:
            u=(previous/2)+1
            v=1
            print(round(u),v)
    else:
        if k%2==0:
            if previous%2==0:
                u=previous/2
                v=2
                print(round(u),v)
            else:
                u=(previous/2)+1
                v=1
                print(round(u),v)
        else:
            if previous%2==0:
                u1=previous/2
                v1=2
            else:
                u1=(previous/2)+1
                v1=1
            if after%2==0:
                u2=after/2
                v2=2
            else:
                u2=(after/2)+1
                v2=1
            if n-u1 <= u2-n:
                print(round(u1),v1)
            else:
                print(round(u2),v2)
