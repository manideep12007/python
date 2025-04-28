# removing all duplicates from the string 

def no_duplicated_string(strng):
    res = []
    words = strng.split()
    for word in words:
        if word not in res :
            res.append(word)
    return " ".join(res) 

strng = "Hello python developers i am also python developer too"
print(no_duplicated_string(strng))