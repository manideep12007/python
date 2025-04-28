# REVERSE OF THE NUMBER 
# 123 to 321 

def reverse_number(number):
    reverse = 0 
    while number != 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
    return reverse

lst = [344,21,456,678]
for num in lst:
    reverse = reverse_number(num)
    print(f"Reverse of {num} is {reverse}")