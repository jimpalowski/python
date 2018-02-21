# Returning the acronym of the string

str = "what is this even about"

def str_capital(string):
    str3 = string[0]

    for x in range(len(string)):
        if string[x - 1] == " ":
            str3 += string[x]
    return str3.upper()
print(str_capital(str))    