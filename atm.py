
withdraw, balance=input().split()
withdraw=int(withdraw)
balance=float(balance)

if(withdraw %5==0 and balance>=(withdraw+0.50)):
    balance=balance-(withdraw+0.50)
    print('{0:.2f}'.format(balance))
else:
    print('{0:.2f}'.format(balance))
