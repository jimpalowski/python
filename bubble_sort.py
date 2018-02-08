import random

items = [random.randint(-50, 100) for r in range(10)]


def bubble_sort(items):
    for x in range(len(items)-1):
        for y in range(len(items)-1-x):
            if items[y] > items[y+1]:
                items[y], items[y+1] = items[y+1], items[y]
    return items

print('before', items)
bubble_sort(items)
print('after', items)      


bubble_sort(items)      