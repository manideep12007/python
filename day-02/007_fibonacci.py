# fibonacci series 

def fibonacci(num):
    a,b = 0,1
    if num <= 0:
        return []
    elif num == 1:
        return [a]
    series = [a,b]
    i = 2 
    while i <= num:
        val = a + b 
        series.append(val)
        a = b 
        b = val
        i += 1
    return series

print(fibonacci(10))