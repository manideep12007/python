def greatest(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum :
            maximum = num 
    return maximum 

lst = [34,24,12,35,22]
print(f"The greatest element of the {lst} is {greatest(lst)}")

# similarly lessthan 
def lessthan(lst):
    minimum = lst[0]
    i = 0
    while i < len(lst):
        if lst[i] < minimum:
            minimum = lst[i]
            i += 1
        i += 1 
    return minimum

print(f"The lowest element of the {lst} is {lessthan(lst)}")
