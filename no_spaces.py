str1 = "how is the weather out there"

def no_spaces(string):
    str2 = ""
    for x in string:
        if x == " ":
            pass
        else:
            str2 = str2 + x
    return str2     

print(no_spaces(str1))        