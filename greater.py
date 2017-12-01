#Find the max number in the list of numbers
my_list = [23, 3, 6, 96, -4, 1, 72, 5, 8, ]
def largest_num():
    max = 0
    for x in my_list:
        if x > max:
            max = x
    print(max)

largest_num()

#Find the min number in the list of number
def smallest_num():
    low= 0
    for x in my_list:
        if x < low:
            low = x
    print(low)

smallest_num()