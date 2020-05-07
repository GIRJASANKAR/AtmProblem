t=int(input())
count=0
for i in range(t):
    n=int(input())
    l=[100,50,10,5,2,1]
    while(n!=0):
        for j in l:
            if(n%j==0):
                count+=n//j

                n=n%j
            else:
                count+=n//j

                n=n%j
        print(count)
        count=0



