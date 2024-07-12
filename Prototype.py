"""
The Prototype design pattern is a creational pattern that allows you to create new objects 
by copying an existing object, known as the prototype. This pattern is useful when the cost of 
creating a new object is more expensive or complex than copying an existing one.
"""

import copy

# Prototype interface: Defines the cloning method
class Protoype:
    def clone(self):
        return copy.deepcopy(self)

# Concrete prototypes: Implement the cloning method 
class ConcretePrototype(Protoype):
    def __init__(self, value):
        self.value = value

#Client: Creates new objects by asking a prototype to clone itself.
prototype = ConcretePrototype(10)
clone = prototype.clone()
clone.value = 20

print(f'Original: {prototype.value}')
print(f'Cloned copy: {clone.value}')

""" 
Benefits of the Prototype pattern:
1.Reduces subclassing
2.Hides complexities of creating new instances
3.Allows adding or removing products at runtime

Common use cases:

1.When a system should be independent of how its products are created and composed
2.When classes to instantiate are specified at runtime
"""