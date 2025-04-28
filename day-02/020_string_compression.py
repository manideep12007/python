# string compression 
# aaab -> a3b

def string_compression(s):
    if not s:
        return ""
    res = []
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            res.append(s[i-1] + str(count))
            count = 1
    res.append(s[-1] + str(count))
    return "".join(res) if len("".join(res)) < len(s) else s 

print(string_compression("abbc"))