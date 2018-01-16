my_dict = {
"Speros": "(555) 555-5555",
"Michael": "(999) 999-9999",
"Jay": "(777) 777-7777"
}

def atr(my_dict):
  x = my_dict.keys()
  y = my_dict.values()
  z = zip(x,y)
  print z


atr(my_dict)