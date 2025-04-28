# counting vowels in the given string 
def count_vowels(strng:str):
    count = 0
    for letter in strng.lower():
        count += 1 if letter in 'aeiou' else 0
    return count

strng = input("Enter any string: ")
print(count_vowels(strng))