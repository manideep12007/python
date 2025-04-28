# factorial of a number 
# 0! = 1 
# 1! = 1 
# 2! = 2 * 1 = 2 
# 3! = 3 * 2 * 1 = 6 

# normal way 
def factorial(n):
    fact = 1
    if n == 0:
        return fact
    else:
        for i in range(1,n+1):
            fact *= i
        return fact 

print(f"Factorial of 5 is {factorial(5)}")
print(f"Factorial of 4 is {factorial(4)}")

# recursive manner 
# tail 
def factorial_recur(num,fact=1):
    if num == 0 :
        return fact
    return factorial_recur(num - 1,fact= num * fact)

print(f"Factorial of 3 is {factorial_recur(3)}")
print(f"Factorial of 2 is {factorial_recur(2)}")

# head 
def factorial_recur_2(num):
    if num == 0:
        return 1 
    return num * factorial_recur_2(num-1)

print(f"Factorial of 1 is {factorial_recur_2(1)}")
print(f"Factorial of 0 is {factorial_recur_2(0)}")