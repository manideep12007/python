# palindrome string 
# aaa == aaa 
# abc != cba

def is_palindrome(strng:str):
    rev = ''
    for char in strng:
        rev = char + rev
    return rev == strng

print(is_palindrome("Python World"))
print(is_palindrome("madam"))
