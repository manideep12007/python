# hollow rectangle 
""" 

*****
*   *
*   *
*****


"""

def hollow_rectangle(length,breadth):
    for i in range(length):
        for j in range(breadth):
            if i == 0 or i == length-1 or j == 0 or j == breadth - 1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

length = 4 
breadth = 5
hollow_rectangle(length,breadth)