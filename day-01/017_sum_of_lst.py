# sum of elements in the list 

def sum_of_ele(lst):
    result = 0 
    for ele in lst:
        result += ele 
    return result

lst = [12,45,23,12]
print(f"Sum of elements in {lst} is {sum_of_ele(lst=lst)}")