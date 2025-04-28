# substring present in string or not 

# def substr_in_str(strng,target):
#     return True if target in strng else False

# print(substr_in_str("geeks for geeks","geeks"))

def substr_in_str(strng,target_list):
    strng_list = strng.split()
    return all(target in strng_list for target in target_list)

strng = "Hello world of python Hello"
target = ["hello","world"]
print(substr_in_str(strng,target))