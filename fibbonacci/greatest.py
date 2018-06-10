#python 3

n=int(input())

a=[int(k) for k in input().split()]
a=sorted(a)
maximum=0
if(len(a)==n):
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]*a[j]>maximum:
                maximum=a[i]*a[j]
                continue
    print(maximum)
