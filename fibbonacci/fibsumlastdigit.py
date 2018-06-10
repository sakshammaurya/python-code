#python3
n=input()
n=int(n)


modlist=[]
def fibmodulo(n:'upto n number')->int:
    if n<=0:
        return n
    a=0
    b=1
    d=1
    fibo=[a,b]
    for i in range(0,n-1):
        b=a+b
        a=b-a
        c=b%10
        d=d+c
        #fibo.append(c)
    return d%10
print(fibmodulo(n))
