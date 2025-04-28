# Armstrong number 
# number is equal to sum of digits to power to its number of digits
# 153 = 1**3 + 5**3 + 3**3 = 153 

def is_armstrong(number):
    temp = number
    count = result = 0 
    while temp != 0:
        temp //= 10 
        count += 1
    temp = number
    while temp != 0:
        digit = temp % 10 
        result += digit ** count
        temp //= 10 
    return number == result

for i in range(101,501):
    print(i,end=" ") if is_armstrong(i) else ''
else:
    print("\nThese are armstrong numbers between 101 and 500")