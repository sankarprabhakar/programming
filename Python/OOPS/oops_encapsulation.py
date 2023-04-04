## Data encapsulation:  Encapsulation refers to
#  the bundling of attributes and methods inside a single class. 
#  It is also know as data hiding

class Dog:
    __voice = "no" ## double underscore is used to define private variables
    def __init__(self):
        self.__voice = "whoof whoof"
    def bark(self):
        print(self.__voice)
    def setBarkSound(self, sound):
        self.__voice = sound

dog1 = Dog()
dog1.__voice = "hddd" ;## it wont work, as __voice is private variable
dog1.bark()
