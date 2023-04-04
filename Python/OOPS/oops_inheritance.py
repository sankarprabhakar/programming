# Inheritance is a way of creating a new class for using details of an
#  existing class without modifying it.

class Animal:
    def __init__(self):
        self.value=66
        print("Animal class init called")
    def eat(self):
        print("I eat {} eggs".format(self.value))
    def sleep(self):
        print("I sleep")

class Dog(Animal):
    def __init__(self):
        print("Dog init called")
        Animal.__init__(self) ## this also works!!
        #super(Dog,self).__init__() ## this is to call the super class constructor.
    def bark(self):
        print("I bark bow booow ")


dog1 = Dog()
dog1.bark()
dog1.eat()
