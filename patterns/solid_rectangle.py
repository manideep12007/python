# solid rectangle pattern 

""" 

*****
*****
*****
*****


"""

def solid_rectangle(length,breadth):
    for i in range(length):
        for j in range(breadth):
            print("* ",end=" ")
        print()
    
rows = 4 
cols = 5 
solid_rectangle(length=rows,breadth=cols)