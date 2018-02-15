
#Return 2nd largest value from List1 and List2
list1 = [1, 9, 34, -42, -18, 95, -1, 14]
list2 = [41, 28, 15, 35, 32, 9, 81]


# Return the values from index 3 to index 5 from both List1 and List 2

def large_val(list1, list2):
    nm1 = list1[0]
    max = list1[0]
    nm2 = list2[0]
    max2 = list2[0]

    for x in range(len(list1)):
        if list1[x] > max:
            max = list1[x]

    for y in range(len(list1)):
        if list1[y] > nm1 and list1[y] < max:
            nm1 = list1[y]

    for i in range(len(list2)):
        if list2[i] > max2:
            max2 = list2[i]

    for j in range(len(list2)):
        if list2[j]>nm2 and list2[j] < max2:
            nm2 = list2[j]
    return(nm1, nm2)
print(large_val(list1, list2))    
