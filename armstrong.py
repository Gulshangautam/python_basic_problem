n=407
sum=0
num=n
while(n>0):
    rem=n%10
    sum=sum+(rem**3)
    n=n/10
if(sum==num):
    print("armstrong")
else:
    print("consugate")        