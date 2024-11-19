# The Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate.
#  Factory Method lets a class defer instantiation to subclasses.

from abc import ABC, abstractmethod

#Abstract Product
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass  

#Concrete Product implementing abstract product interface
class BeefBurger(Burger):
    #define prepare method 
    def prepare(self):
        print("Preparing BeefBurger....")

#Concrete Product implementing abstract product interface
class VeggieBurger(Burger):
    def prepare(self):
        print("Preparing VeggieBurger....")




#Abstract Factory/Creator
class BurgerRestaurant(ABC):
    def orderBurger(self):
        print("Ordering Burger....")
        burger = self.createBurger()  # abctract method to create product
        burger.prepare() #Prepare product 
    
    @abstractmethod
    def createBurger(self)->Burger:
        pass 
    
#Concrete Factory implementing abstract factory. Concrete factory decide which abstract product class to instantiate.
class BeefBurgerRestaurant(BurgerRestaurant):
    def createBurger(self) -> Burger:
        print("Creating Beef Burger in BeefBurgerRestaurant....")
        return BeefBurger() 

class VeggieBurgerRestaurant(BurgerRestaurant):
    def createBurger(self) -> Burger:
        print("Creating Veggie Burger in VeggieBurgerRestaurant...")
        return VeggieBurger()


def main():
    beefBurgerRestaurant =  BeefBurgerRestaurant()  #create a BeefBurgerRestaurant of type Restaurant
    beefBurgerRestaurant.orderBurger()


    print("------------------------------")

    veggieBurgerRestaurant = VeggieBurgerRestaurant()  #create a ViggeBurgerRestaurant of type Restaurant 
    veggieBurgerRestaurant.orderBurger()



if __name__ == "__main__":
    main()