# checking prime or not  

# general way 
def isPrime_gen(number):
    if number > 1:
        for i in range(2,int(number ** 0.5)+1):
            if number % i == 0 :
                return False 
        return True 
    return False


# optimized version 
def isPrime(number):
    # eliminating lessthan or equal to one
    if number <= 1 :
        return False
    # returns True for 2 and 3
    if number <= 3:
        return True
    # eliminating even and odd numbers 
    if number % 2 == 0 or number % 3 == 0:
        return False
    # starting checking condition from 5
    i = 5 
    # looping till i square less than or equal to number 
    while i ** 2 <= number:
        # if alternative i values are satisfied eliminating 
        if (number % i == 0) or (number % (i+1) == 0):
            return False
        # incrementing by 6 (as numbers of the form 6k ± 1 need to be checked)
        i += 6
    # remaining situation results True 
    return True

# for num in range(1,31):
#     print(num,end=" ") if isPrime(num) else ''
# else:
#     print("\nThis are prime numbers between 1 to 31")

for num in range(1,31):
    print(num,end=" ") if isPrime_gen(num) else ''
else:
    print("\nThese are prime numbers between 1 and 31")
