# Return a new list that is the combination of list1 and list2.
# Alternate between both lists(take first value from list1/ next value from list2) Any extra values can be put at the end of the list


list1 = [1, 9, 34, -42, -18, 95, -1, 14]
list2 = [41, 28, 15, 35, 32, 9, 81]

def merge(list1, list2):
    list3= []
    num = max(len(list1), len(list2))
    for x in range(0, num):
        if x <=len(list1)-1 and x <=len(list2)-1:
            list3.append(list1[x])
            list3.append(list2[x])
            print (list3)
        if x > len(list2) - 1 and x <= len(list1) - 1:
            list3.append(list1[x])
            print(list3)
        if x > len(list1) - 1 and x <=len(list2) - 1:
            list3.append(list2[x])
            print(list3)
    return list3            

print (merge(list1, list2))



# Return the combination of list 1 and list 2 again, but using list 1 as the return instead of a new list

 

'''list1 = [1, 9, 34, -42, -18, 95, -1, 14]
list2 = [41, 28, 15, 35, 32, 9, 81, 78, 90, 99, 76]

def merge(list1, list2):
    num = min(len(list1), len(list2))
    temp = [None] * (num*2)
    temp[::2] = list1[:num]
    temp[1::2] = list2[:num]
    temp.extend(list1[num: ])
    temp.extend(list2[num: ])
    list1 = temp
    return list1
print (merge(list1, list2)) '''