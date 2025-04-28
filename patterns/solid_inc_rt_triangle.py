# solid right angled triangle 
# increasing 

""" 

*
**
***
****
*****


"""

def right_angled_increasing_triangle(n):
    for i in range(n):
        print("* "*(i+1))
    
n = 5 
right_angled_increasing_triangle(n=n)