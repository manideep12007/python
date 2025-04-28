# half pyramid shape 
# decreading space triangle + increasing solid triangle

""" 
    *
   **
  ***
 ****
*****

"""

def half_pyramid(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
    
half_pyramid(5)