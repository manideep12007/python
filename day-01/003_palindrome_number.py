# palindrome number 
# number which is equal to reverse of its digits
# 101 = 101 but not 123 != 321

def is_palindrome(num):
    temp = num
    reverse = 0 
    while temp != 0:
        digit = temp % 10 
        reverse = reverse * 10 + digit
        temp //= 10 
    return num == reverse

for i in range(100,125):
    print(f"{i} is palindrome number!") if is_palindrome(i) else ''