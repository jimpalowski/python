import itertools

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]

favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(name, favorite_animal):
    new_dict  = dict(itertools.izip(name, favorite_animal))
    print new_dict

make_dict(name, favorite_animal)