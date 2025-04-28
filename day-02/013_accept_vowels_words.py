# accepting string of words with vowels 
import string
def vowels_string(strng):
    strng_lst = strng.split()
    res = []
    for word in strng_lst:
        # is_vowel = True
        # for char in word.lower():
        #     if char not in "aeiou":
        #         is_vowel = False
        #         break
        # if is_vowel:
        #     res.append(word)
        # if any(char in 'aeiou' for char in word.lower()):
        #     res.append(word)
        if all(char in "aeiou" for char in word.lower()):
            res.append(word)
    return " ".join(res)

strng = "Hello world of python the! aei !!"
print(vowels_string(strng))
