my_list = ["hello", "welcome", "good", "morning", "night", "we", "i", "too"]

def return_strings(list):
  list2 = []
  for x in range(len(list)):
    if (len(list[x]) > 4):
      list2.append(list[x])
  return list2    
  
  
print(return_strings(my_list)) 