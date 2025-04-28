# even numbers in the list 

def even_lst(lst):
    return [x for x in lst if x % 2 == 0]

lst = [x for x in range(1,21)]
even_lst = even_lst(lst)
print(even_lst)