# floyd's triangle 

""" 
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""

def floyd_triangle(n):
    val = 1
    for i in range(n):
        for j in range(i+1):
            print(val,end=" ")
            val += 1
        print()

floyd_triangle(5)