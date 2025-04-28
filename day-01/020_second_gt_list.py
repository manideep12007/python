# program to find the second largest number in a list.

def second_largest(lst):
    for i in range(len(lst)):
        maximum = i 
        for j in range(i+1,len(lst)):
            if lst[maximum] < lst[j]:
                maximum = j 
        lst[maximum],lst[i] = lst[i],lst[maximum]
    return lst[1]

lst = [23,45,6,34,23]
print(second_largest(lst))
