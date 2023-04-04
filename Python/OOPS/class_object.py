## Class is blue print for object
## created using class keyword
## class will have attributes and methods
## EXAMPLE OF CLASS BIKE 

class Bike:
    name = ""
    gear = 0
    ## Constructor for Bike Class
    def __init__(self,name, gear):
        print("Constructor is called")
        self.name = name
        self.gear = gear
    
    def print_bike_name(self):
        print(self.name)
    def print_bike_gear(self):
        print(self.gear)

## Crate object 
bike1 = Bike("Royal Enfield",4)
bike2 = Bike("Yamaha RX100",3)

print(bike1.print_bike_gear(), bike1.print_bike_name())
print(bike2.print_bike_gear(), bike2.print_bike_name())
