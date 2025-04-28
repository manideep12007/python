# right angled decreasing triangle 

""" 
*****
****
***
**
*


"""

def right_angled_triangle(n):
    for i in range(n+1):
        print("* "*(n-i))
    
n = 5 
right_angled_triangle(n)