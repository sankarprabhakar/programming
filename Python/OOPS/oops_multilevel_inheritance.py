class BaseClass:
    def info(self):
        print("we are base class")
    def info_BaseClass(self):
        print("info_BaseClass")
class DerivedClass1(BaseClass):
    def info(self):
        print("Im  derived class 1")
    def info_DerivedClass1(self):
        print("DerivedClass1")
class DerivedClass2(DerivedClass1):
    def info(self):
        print("Im derived Class 2")
    def info_DerivedClass2(self):
        print("DerivedClass2")


obj = DerivedClass2()
## methods of all the levels of classes are visible
obj.info()
obj.info_DerivedClass1()
obj.info_DerivedClass2()