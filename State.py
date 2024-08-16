"""  
The State design pattern is a behavioral design pattern that allows an object 
to alter its behavior when its internal state changes. 
"""

from abc import ABC, abstractmethod

#Context: The object whose behavior changes
class VendingMachine:
    def __init__(self):
        self.idle_state = IdleState()
        self.has_coin_state = HasCoinState()
        self.product_selected_state = ProductSelectedState()
        self.state = self.idle_state
        
    def setState(self, state):
        self.state = state
    
    def insertCoin(self):
        self.state.insertCoin(self)
    def selectProduct(self):
        self.state.selectProduct(self)
    def dispenseProduct(self):
        self.state.dispenseProduct(self)

#State interface: Defines methods for state-specific behavior
class VendingMachineState(ABC):
    @abstractmethod
    def insertCoin(self, machine):
        pass
    @abstractmethod
    def selectProduct(self, machine):
        pass
    
    @abstractmethod
    def dispenseProduct(self, machine):
        pass

#Concrete states: Implement the State interface
class IdleState(VendingMachineState):
    def insertCoin(self,machine):
        print("Coin inserted")
        machine.setState(machine.has_coin_state)
    
    def selectProduct(self, machine):
        print("Please insert coin first")
    
    def dispenseProduct(self, machine):
        print("Please insert a coin and select a product first")
#Concrete states: Implement the State interface
class HasCoinState(VendingMachineState):
    def insertCoin(self, machine):
        print("Your have already inserted coin")
    def selectProduct(self, machine):
        print("Product Selected")
        machine.setState(machine.product_selected_state)
    def dispenseProduct(self, machine):
        print("Please select a product first")
#Concrete states: Implement the State interface
class ProductSelectedState(VendingMachineState):
    def insertCoin(self, machine):
        print("You've already inserted a coin")

    def selectProduct(self, machine):
        print("You've already selected a product")

    def dispenseProduct(self, machine):
        print("Product dispensed")
        machine.setState(machine.idle_state)

#Client Code       
machine = VendingMachine()
machine.insertCoin()
machine.selectProduct()
machine.dispenseProduct()


"""  
1.A VendingMachine class that maintains a current state and delegates actions to i
2. A VendingMachineState abstract base class defining the interface for all states.
3.Concrete state classes (IdleState, HasCoinState, ProductSelectedState) implementing state-specific behavior.


Benefits:
Organizes state-specific code
Makes state transitions explicit
Allows new states to be added easily
"""