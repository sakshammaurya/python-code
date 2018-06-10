#python3
n=int(input())
a=map(int,input().split())
lst=[]
for i range(0,n):
    for j in range(i+1,n):
        if a[i]<10:
            lst.append(a[i])
        if 10<a[i]<100:
            k=a[i]//10
        if 100<a[i]<1000:
            m=a[i]//100
        
      
