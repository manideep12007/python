# print all primes in given range 

def printAllprimes(a,b):
    for num in range(a,b+1):
        is_prime = True
        if num > 1:
            for i in range(2,int(num**0.5)+1):
                if num % i == 0:
                    is_prime = False
                    break
        else:
            is_prime = False
        if is_prime:
            print(num,end=" ")
    print(f"\nThese are prime numbers in between {a} and {b}.")
printAllprimes(a=50,b=150)