number=int(input("Enter a number:"))
total=0
number=number*3
number=number+1
print("The number now is:",number)
while(number>9):
    dig=number%10
    total=total+dig
    print("The sum is:",total)
    number=number//10
    print("The number now is:",number)
    number=number*3
    number=number+1
    print("The number now is:",number)
print("The total sum of digits is:",total)
