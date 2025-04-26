# product of elements in the list 

def product_of_elements(lst):
    result = 1
    for ele in lst:
        result *= ele 
    return result

lst = [12,45,23,12]
print(f"Product of elements in {lst} is {product_of_elements(lst=lst)}")