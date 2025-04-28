# integer to binary number 0's and 1's

# direct approach 
def binary(num:int):
    return bin(num)[2:]

# manual way 
def binary_gen(num:int):
    res = sign = ''
    if num < 0:
        sign = '-'
        num = -num
    if num == 0:
        return '0'
    while num != 0:
        res =  str(num % 2) + res 
        num //= 2 
    return sign + res 

print(f"binary of 10 is {binary(10)}")
print(f"binary of 11 is {binary_gen(11)}")
print(f"binary of -11 is {binary_gen(-11)}")
