# numbers triangle 
"""  
1
12
123
1234
12345

"""

def numbers_triangle(n):
    for i in range(n):
        for j in range(i+1):
            val = j + 1
            print(val,end=" ")
        print()
    
numbers_triangle(5)
