import numpy as np

t=int(input())
for i in range(t):
    n=int(input())
    b=[]
    flag=0
    for j in range(n):
        a=list(map(int,input().split()))
        b.append(a)
    b.sort()
    jo=-1
    co=-1
    jc=-1
    cc=-1
    y=0
    c = np.zeros((n,4),dtype=int)
    #print(c)
    c[0][2]=1
    for j in range(n):
        c[j][0]=b[j][0]
        c[j][1]=b[j][1]
    jo=c[0][0]
    jc=c[0][1]
    j=1
    while co==-1 and j<n:
        if jc<=c[j][0]:
            jc=c[j][1]
            jo=c[j][0]
            c[j][2]=1
        else:
            co=c[j][0]
            cc=c[j][1]
            c[j][2]=2
        j+=1
        y=j

    for j in range(y,n):
        if jc<=c[j][0]:
            jc=c[j][0]
            jo=c[j][0]
            c[j][2]=1
        elif cc<=c[j][0]:
            co=c[j][0]
            cc=c[j][1]
            c[j][2]=2
        else:
            flag=-1
    ans=""
    if flag == -1:
        ans="IMPOSSIBLE"
    else:
        for j in range(n):
            for k in range(n):
                if b[j][0]==c[k][0] and b[j][1]==c[k][1] and c[k][3]==0:
                    if c[k][2] == 1:
                        ans += 'C'
                    else:
                        ans += 'J'        
    print("Case #"+str(i+1)+": "+ans)
    i+=1
