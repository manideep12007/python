# numbers triangle 

""" 
1
22
333
4444
55555

"""

def numbers_triangle(n):
    for i in range(n):
        for j in range(i+1):
            val = i + 1
            print(val,end="")
        print()
    
numbers_triangle(5)