n, k=input().split()
n=int(n)
k=int(k)
count=0
for i in range(n):
    a=int(input())
    if(a%k==0):
        count+=1
print(count)


