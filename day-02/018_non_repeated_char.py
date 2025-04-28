# finding non-repeated character in a sting 

def non_repeated_character(word):
    d1 = {}
    for char in word:
        if char.isalpha():
            if char not in d1:
                d1[char] = 1
            else:
                d1[char] += 1
    for char in word:
        if d1[char] == 1:
            return char 
    return -1 

print(non_repeated_character("swwiiss"))