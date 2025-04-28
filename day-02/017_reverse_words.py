# reverse the words order 
def reverse_strng(strng):
    res = []
    for word in strng.split():
        res.insert(0,word)
    return ' '.join(res)

input_strng = "Hello world from python"
print(reverse_strng(input_strng))