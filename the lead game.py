n=int(input())
ts,tt=0,0
leader,lead=0,0
max=0
for i in range(n):
    s,t=map(int,input().split())
    ts+=s
    tt+=t
    if(ts>tt):

        lead=ts-tt
        if(max<lead):
            max=lead
            leader=1
    else:

        lead=tt-ts
        if(max<lead):
            max=lead
            leader=2
print(leader,' ',max)

