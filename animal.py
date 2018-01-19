class Animal():
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health-1
        return self

    def run(self):
        self.health = self.health-5
        return self

    def display_health(self):
        print "Name: {} | Health: {}".format(self.name, self.health)
        return self

animal1 = Animal("Jack")

animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        self.health = 150
        self.name = name

    def pet(self):
        self.health += 5
        return self
dog1 = Dog("Rocky")
dog1.walk().walk().walk().run().run().pet().display_health()   



class Dragon(Animal):
    def __init__(self, name):
        self.name = name
        self.health = 170

    def fly(self):
        self.health-=10
        return self

    def display_health(self):
        print "I am a Dragon"
        return self

dragon1 = Dragon("Alduin")        
dragon1.walk().walk().walk().run().run().fly().fly().display_health()


class Orca(Animal):
    def __init__(self, name):
        self.name = name

orca1 = Orca("Shamoo")
orca1.pet()
orca1.fly()
orca1.displayHealth()

dog1.fly()