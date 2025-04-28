# removing duplicates from the list 

def no_duplicates_list(lst):
    res = []
    for ele in lst:
        res.append(ele) if ele not in res else ''
    return res 

lst = [11,11,23,12,22,23]
res = no_duplicates_list(lst)
print(res)