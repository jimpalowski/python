def del_copies(str):
    dict = {}
    new_str = ''
    for x in range(len(str)):
        for y in str:
            if y != ' ':
                dict[y] = None
    for x in dict:
        new_str += x 
    return new_str


str = "Hola Mundo"
print(del_copies(str))            