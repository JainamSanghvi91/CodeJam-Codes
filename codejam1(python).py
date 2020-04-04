import numpy as np

t=int(input())
for w in range(t):
    a=[]
    row=0
    tra=0
    col=0
    n=int(input())
    for j in range(n):
        temp = input()
        b = list(map(int,temp.split()))
        a.append(b)
    mat = np.array(a)
    #print(mat)
    for i in range(len(mat)):
        sr=set(mat[i])
        if len(sr) != len(mat[i]):
            row+=1
        else:
            continue
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i==j:
                tra += mat[i][j]
            else:
                continue
    mat1=mat.transpose()
    for i in range(len(mat1)):
        sc=set(mat1[i])
        if len(sc) != len(mat1[i]):
            col+=1
        else:
            continue
    print("Case #{}: {} {} {}".format(w+1,tra,row,col))
