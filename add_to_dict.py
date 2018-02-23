my_list = [3, 5, 6, 7, 10, 15]

def MaxMinAvg(list):
    obj = {'max': list[0], 'min': list[0], 'avg': 0}
    sum = 0
    for x in range(len(list)):
        if list[x] > obj['max']:
            obj['max'] = list[x]
        if list[x] < obj['min']:
            obj['min'] = list[x]
        sum += list[x]
        obj['avg'] = sum/len(list)
    return obj 

print(MaxMinAvg(my_list))           

#Adding Max, Min, Average to a dictionary