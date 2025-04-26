# anagrams - if two strings uses same length and words to generate different word

def anagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    d1 = {}
    d2 = {}
    for char in s1:
        if char in d1:
            d1[char] += 1
        else:
            d1[char] = 1
    for char in s2:
        if char not in d2:
            d2[char] = 1
        else:
            d2[char] += 1
    return d1 == d2 

s1 = 'light'
s2 = 'tight'
print(anagrams(s1,s2))
print(anagrams("listen","silent"))