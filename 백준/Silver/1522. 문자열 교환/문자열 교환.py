def string_exchange(string):
    a_n = string.count("a")
    if a_n == 0 | len(string):
        return 0
    string += string
    b_n = string[:a_n].count("b")
    res = b_n
    
    for i in range(len(string)//2 - 1):
        b_n += (string[i+a_n]=="b") - (string[i]=="b")
        res = min(res , b_n)
    
    return res

string = input()
print(string_exchange(string))