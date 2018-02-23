my_str = "reversing"
def other_string(string):
    new_str = string[0]
    final_string = ""
    for x in range(len(string)-2, -1, -2):
        new_str += string[x]
    for y in range(len(new_str)-1, 0, -1):
        final_string += new_str[y]
    return final_string
print(rev(my_str)) 

#Returning any other letter in a string