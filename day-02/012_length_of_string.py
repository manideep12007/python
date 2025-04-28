# finding the length of the string 

def length_of_string(string):
    length = 0 
    for _ in string:
        length += 1
    return length

print(f"Length of string is {length_of_string("Hello Python world!")}")