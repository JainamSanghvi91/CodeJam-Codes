t=int(input())
cou=1
for i in range(t):
    s=input()
    l=int(s[0])
    ans=""
    for i in range(l):
        ans += '('
    if len(s)==1:
        ans += s[0]
    else:
        for j in range(len(s)-1):
            d=int(s[j+1])-int(s[j])
            l += d
            if d>0:
                ans += s[j]
                for k in range(abs(d)):
                    ans += '('
            elif d<0:
                ans += s[j]
                for k in range(abs(d)):
                    ans += ')'
            else:
                ans += s[j]
                continue
        ans += s[j+1]
    for i in range(l):
        ans += ')'
    print("Case #{}: {}".format(cou,ans))
    cou+=1
