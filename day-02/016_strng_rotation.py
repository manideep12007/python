# string rotation 

def rotate_string(strng,d):
    return strng[d:]+strng[:d],strng[-d:] + strng[:-d]
    # left rotatation , right rotation 

strng = "Hellopython"
left,right = rotate_string(strng,5)
print(left)
print(right)