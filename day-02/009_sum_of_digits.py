# sum of digits of the number 

def sum_of_digits(num):
    sum = 0
    while num != 0:
        digit = num % 10 
        sum += digit
        num //= 10
    return sum 
n = 12345
print("Thes sum of digits of {} is {}".format(n,sum_of_digits(n)))