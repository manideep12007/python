# lcm or least common multiple of two numbers
# gcd or greatest common divisor of two numbers 

def gcd(a,b):
    while b != 0:
        a,b = b,a % b 
    return a 

def lcm(a,b):
    return abs(a * b) // gcd(a,b)

print(f"The GCD OF 12,17 IS {gcd(12,17)}")
print(f"The LCM OF 12,17 IS {lcm(12,17)}")
