#python3
n,m=input().split()
n=int(n)
m=int(m)

modlist=[]
def fibmodulo(n:'upto n number')->int:
    if n<=0:
        return n
    a=0
    b=1
    fibo=[a,b]
    for i in range(0,100000):
        b=a+b
        a=b-a
        fibo.append(b)
    for x in fibo:
        mod=x%m
        modlist.append(mod)
    d=len(modlist)
    for y in range(1,d):
        if modlist[0:y]==modlist[y:2*y]:
            break
    f=n%y
    if f<=1:
        return f
    r=0
    t=1
    for h in range(0,f-1):
        t=r+t
        r=t-r
    p=t%m
        
    return p
print(fibmodulo(n))


