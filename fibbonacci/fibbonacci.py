#python3
n=int(input())
def fib(n:'upto n nnumber')->int:
    if n==0:
        return 0
    elif n==1:
        return 1
    a=0
    b=1
    for i in range(0,n-1):
        b=a+b
        a=b-a
    return b
print(fib(n))

