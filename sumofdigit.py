number=121
digit_sum=0
digit=0
while(number!=0):
    digit=number%10
    digit_sum=digit_sum+digit
    number=number//10
print(digit_sum)