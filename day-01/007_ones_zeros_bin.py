# counting one's and zero's in binary 

def count_ones_zeros(num:int):
    counter = {}
    if num == 0:
        counter["0"] = 1 
        return counter
    if num < 0:
        num = -num 
    while num != 0:
        val = str(num % 2)
        if val not in counter:
            counter[val] = 1
        else:
            counter[val] += 1
        num //= 2
    return counter
num = int(input("Enter the integer: "))
print(count_ones_zeros(num))