# counting consonants in the given string 
def count_consonants(strng:str):
    count = 0
    for letter in strng:
        count += 1 if letter.lower() not in 'aeiou' and letter.isalpha() else 0
    return count

strng = input("Enter any string: ")
print(count_consonants(strng))