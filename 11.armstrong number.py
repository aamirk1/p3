num = int(input("enter number: "))
temp = num
while temp>0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print("arm")
else: 
    print('not') 