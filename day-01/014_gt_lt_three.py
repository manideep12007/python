# finding lessthan and greaterthan of three

def gt(n,m,o):
    return n if n > m and n > o else m if m > o else o 

def lt(n,m,o):
    return n if n < m and n < o else m if m < o else o

print(gt(12,55,23))
print(lt(12,55,23))