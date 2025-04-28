# finding even length words

def even_length_words(strng):
    lst = strng.split()
    res_lst = []
    for word in lst:
        word = word.strip("!~()[]$#")
        res_lst.append(word) if len(word) % 2 == 0 else ''
    return " ".join(res_lst)
strng = "Hi myself john cena from wwe! I am 17x undisputed wrestling champion"
print(even_length_words(strng))