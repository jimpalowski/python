def chice[list1]:
    result=list(filter((lambda x:x%2 == 0), list1))
    return result
print(chice(range(1,100)))