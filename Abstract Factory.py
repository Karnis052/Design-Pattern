#The Abstract Factory Pattern provides an interface for creating families of related or 
# dependent objects without specifying their concrete classes.

from abc import ABC, abstractmethod

#Abstract product: This is one of the product family. Each concrete factory can produce an entire set of products.
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

class VeggieBurger(Burger):
    def prepare(self):
        print("Preparing VeggieBurger....")
class BeefBurger(Burger):
    def prepare(self):
        print("Preparing BeefBurger....")


#Abstract product: This is one of the product family. Each concrete factory can produce an entire set of products.
class Pizza(ABC):
    @abstractmethod
    def bake(self):
        pass 

class VeggiPizza(Pizza):
    def bake(self):
        print("Preparing ViggePizza....")

class BeefPizza(Pizza):
    def bake(self):
        print("Preparing BeefPizza....") 


#Abstract Factory
#The Abstract Factory defines the interface that all Concrete factories must implement, which consists of a set of methods for producing products.
class Restaurant(ABC):
    def orderBurger(self):
        print("Ordering Burger...")
        burger = self.createBurger() 
        burger.prepare()
    def orderPizza(self):
        print("Ordering Pizza...")
        pizza =self.createPizza()
        pizza.bake()
    @abstractmethod
    def createBurger(self)->Burger:
        pass
    @abstractmethod 
    def createPizza(self)->Pizza:
        pass

#Concrete Factory 
#The concrete factories implement the different product families.
#  To create a product, the client uses one of these factories
class VeggieRestaurant(Restaurant):
    def createBurger(self)->Burger:
        print("Veggie Burger is creating...")
        return VeggieBurger() 

    def createPizza(self) -> Pizza:
        print("Veggi Pizza is creating....") 
        return VeggiPizza()

class BeefRestaurant(Restaurant):
    def createBurger(self) -> Burger:
        print("Beef Burger is creating...") 
        return BeefBurger()

    def createPizza(self)->Pizza:
        print("Beef Pizza is creating....") 
        return BeefPizza() 

#Client: The Client is written against the abstract factory and then composed at runtime with an actual factory.
def main():
    beefRestaurant = BeefRestaurant()
    beefRestaurant.orderBurger() 

    print("--------------------------------") 

    beefPizza = BeefRestaurant()
    beefPizza.orderPizza()

if __name__ == "__main__":
    main()