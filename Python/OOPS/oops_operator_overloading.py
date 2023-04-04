## Operator overloading helps to define how an operator works on a given object
## Eample + operator add two integers given . But if the operands are string obj what would be the result?
## How + operator works on strings?  
## For string it concatenates the strings
## How the + operator works on list?
## it joins the list.
## how is these operation acheieved ? It is through operator overloading.

## Operator overloading helps to achieve differnt operations out of operators for differnt contexts.

## Python special function. function with double underscore(__) as prefix and suffix are  
#  called special functions in object. Interpret defines these  special functions to define specific behavior.

## examples
## __init__() --> Constructors
## __call__() --> this function of object is invoked if we invoke object (like function)
## __add__() --> when + function is invoked on a object
## __len__() --> returns len of the object
## __str__() --> returns the string representation of object


#Operator	Expression	Internally
#Addition	p1 + p2	p1.__add__(p2)
#Subtraction	p1 - p2	p1.__sub__(p2)
#Multiplication	p1 * p2	p1.__mul__(p2)
#Power	p1 ** p2	p1.__pow__(p2)
#Division	p1 / p2	p1.__truediv__(p2)
#Floor Division	p1 // p2	p1.__floordiv__(p2)
#Remainder (modulo)	p1 % p2	p1.__mod__(p2)
#Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
#Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
#Bitwise AND	p1 & p2	p1.__and__(p2)
#Bitwise OR	p1 | p2	p1.__or__(p2)
#Bitwise XOR	p1 ^ p2	p1.__xor__(p2)
#Bitwise NOT	~p1	p1.__invert__()
#Less than	p1 < p2	p1.__lt__(p2)
#Less than or equal to	p1 <= p2	p1.__le__(p2)
#Equal to	p1 == p2	p1.__eq__(p2)
#Not equal to	p1 != p2	p1.__ne__(p2)
#Greater than	p1 > p2	p1.__gt__(p2)
#Greater than or equal to	p1 >= p2	p1.__ge__(p2)

from sunau import Au_read


class Square:
    def __init__(self, side):
        self.side = side
        self.area = side * side
    def __add__(self,other): ## add is the function called with + is invoked on the class objects
        return self.area + other.area

sq1 = Square(5)
sq2 = Square(10)
# here the sum of areas of two squares are printed
print(sq1 + sq2)
    




