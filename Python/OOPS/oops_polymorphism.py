## Polymorphism means more than one form 
## Same method will have different forms based on scenario. We implement using 
# funciton overloading

## To invoke super class method (which is overridden) we can use the super().<<method>> 




class Polygon:
    def render(self):
        print("Rendering Polygon..")
class Square(Polygon):
    def render(self):
        ## if we need to call super class render
        super().render()
        print("Rendering Square")
class Rectangle(Polygon):
    def render(self):
        print("Rendering Rectangle")

square = Square()
square.render()
rectangle = Rectangle()
rectangle.render()
