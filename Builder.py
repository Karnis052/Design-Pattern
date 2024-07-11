#Product: The complex object that is being constructed
class Product:  
   def __init__(self):
     self.parts = []
   def add(self, part):
     self.parts.append(part)
   def show(self):
     print("Product parts: ", self.parts) 

# Builder Interface: Define all possible ways to configure product
class Builder:
  def buildPartA(self): pass
  def buildPartB(self): pass
  def getResult(self): pass

#Concrete Builder: Implements the Builder interface and provides 
#specific configurations and steps  
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()
    def buildPartA(self):
       self.product.add("partA")
    def buildPartB(self):
       self.product.add("partB")
    def getResult(self):
       return self.product

# Director: Manage the construction process
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
       self.builder.buildPartA()
       self.builder.buildPartB()


#Client Code: Create a ConcreteBuilder, assign it to the Director and start the construction process.
# Costruction product is then retrieve from builder
builder = ConcreteBuilder()
director = Director(builder)
director.construct()
product = builder.getResult()
product.show()
