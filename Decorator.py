"""
The Decorator design pattern is a structural pattern that allows behavior
to be added to individual objects dynamically without affecting the behavior
of other objects from the same class.

Purpose:
1.Attach additional responsibilities to an object dynamically
2.Provide a flexible alternative to subclassing for extending functionality
"""
#Component: The base interface for objects that can have responsibilities added to them
class Coffee:
    def cost(self):
        pass
    def description(self):
        pass
#Concrete Component: The basic object to which additional responsibilities can be attached
class SimpleCoffee(Coffee):
    def cost(self):
        return 5
    def description(self):
        return "Simple Coffee"
    
#Decorator: Maintains a reference to a Component object and 
# defines an interface that conforms to Component's interface
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee
    def cost(self):
        return self._coffee.cost()
    def description(self):
        return self._coffee.description()
#Concrete Decorator: Adds responsibilities to the component
class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost()+2
    def description(self):
        return f"{self._coffee.description()}, milk "  
#Concrete Decorator: Adds responsibilities to the component
class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost()+1
    def description(self):
        return f"{self._coffee.description()}, sugar"


coffee = SimpleCoffee()
print(f"{coffee.description()} costs ${coffee.cost()}")

milkCoffee = Milk(coffee)
print(f"{milkCoffee.description()} costs ${milkCoffee.cost()}")

sweetMilkCoffee = Sugar(Milk(coffee))
print(f"{sweetMilkCoffee.description()} costs ${sweetMilkCoffee.cost()}")



""" 
This example demonstrates:

1.A base Coffee component
2.A concrete SimpleCoffee implementation
3.A CoffeeDecorator that wraps a Coffee object
4.Concrete decorators Milk and Sugar that add functionality


Benefits:
More flexible than static inheritance
Allows responsibilities to be added and removed at runtime
Avoids feature-laden classes high up in the hierarchy
"""