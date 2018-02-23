my_str = "reversing"
def rev(string):
    new_str = ""
    for x in range(len(string)-1, -1, -1):
        new_str += string[x]
    return new_str

print(rev(my_str))    

#Return a string backwords