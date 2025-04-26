# finding lessthan and greathan of two numbers 

def lessthan(n1,n2):
    return n1 if n1 < n2 else n2

def greaterthan(n1,n2):
    return n1 if n1 > n2 else n2

print(f"The lessthan and greaterthan of 25,17 is")
print(f"{lessthan(25,17)} is lowest")
print(f"{greaterthan(25,17)} is highest")
    