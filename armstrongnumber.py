number=int(input("enter a number"))
sum=0
temp=number
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if number==sum:
    print("your input is an armstrong number")
else:
    print("your input is not an armstrong number")