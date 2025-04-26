# reversing the string 

def reverse_string(strng:str):
    return strng[::-1]

print(reverse_string("Python World"))

def reverse_string(strng:str):
    res = "".join(reversed(strng))
    return res 

print(reverse_string("Python World"))


def reverse_string(strng:str):
    rev = ''
    for char in strng:
        rev = char + rev
    return rev 

print(reverse_string("Python World"))