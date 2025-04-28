# finding second largest element in the list 

def second_largest(lst):
    for i in range(len(lst)):
        max_idx = i 
        for j in range(i+1,len(lst)):
            if lst[j] > lst[max_idx]:
                max_idx = j 
        lst[i],lst[max_idx] = lst[max_idx],lst[i]
    return lst[1]

lst = [ 34,66,12,99,23,56]
print(second_largest(lst=lst))