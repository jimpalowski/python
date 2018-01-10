#Find and Replace
#words = "It's thanksgiving day. It's my birthday, too!"
#print words.replace('day', 'month',1)


#Min and Max

'''list=[2,54,-2,7,12,98]

def tv(list):
    min = 0
    max = 0
    for x in range(0, len(list)):
        if list[x] > max:
            max = list[x]
        if list[x] < min:
            min = list[x]
    print(min, max)
tv(list)    '''


#First and Last
'''list=["hello",2,54,-2,7,12,98,"world"]

def dr(list):
    for x in range(7, len(list)):
        list[x - 6] = list[x]
        if x == len(list) - 1:
            list[x] = 0
    print list

dr(list)'''


#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
new_list = [x[:6]]
new_list.extend(x[6:])
print new_list