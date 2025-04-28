# nth number fibonacci number 

def fibonacci_nth(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_nth(n-1) + fibonacci_nth(n-2)

print(fibonacci_nth(5))
print(fibonacci_nth(4))
print(fibonacci_nth(3))
print(fibonacci_nth(2))
print(fibonacci_nth(1))
print(fibonacci_nth(0))
print(fibonacci_nth(-1))


    