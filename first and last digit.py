'''t=int(input())
for i in range(t):
    arr=[]
    n=int(input())
    while(n!=0):


        f=n%10
        arr.append(f)
        n=n//10

    l=arr[0]
    f=arr[-1]
    print(l+f)'''
t=int(input())
for i in range(t):
    n=str(input())

    a=int(n[0])
    l=int(n[-1])
    sum=(a+l)
    print(sum)




