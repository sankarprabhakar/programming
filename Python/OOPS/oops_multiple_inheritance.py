## A class can be derived from more than one superclass in Python. 
# This is called multiple inheritance.

class Mammal:
    def mammal_info(self):
        print("Mammal Gives birth")
    def eat(self):
        print("I eat xx..")

class WingedAnimal:
    def winged_info(self):
        print("Winged animal can flap")
    def eat(self):
        print("I ear yy")

class Bat(Mammal, WingedAnimal):
    def bat(self):
        print("Bat is a winged mammal")


bat = Bat()
bat.bat()
bat.winged_info()
bat.mammal_info()

bat.eat() ## this will invoke the Mammal eat as Mammal is in the leftmost superclass for Bat
