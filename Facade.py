"""  
The Facade design pattern is a structural pattern that provides a simplified interface to a complex 
subsystem. It encapsulates a set of interfaces in a higher-level interface, making the 
subsystem easier to use.
"""


# Subsystem classes: Implement subsystem functionality and handle work assigned by the Facade object.
class CPU:
    def freeze(self):
        print("Freezing CPU.")
    def jamp(self, position):
        print(f"Jumping to position {position}.")
    def execute(self):
        print("Executing instructions.")

class Memory:
    def load(self, position, data):
        print(f"Loading data '{data}' to position {position}.")
class HardDrive:
    def read(self, lba, size):
        return f"Data from sector {lba} with size {size}."

#Facade: Provides a simple, unified interface to a complex subsystem 
class Facade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hardDrive = HardDrive()
    def start(self):
        self.cpu.freeze()
        data = self.hardDrive.read(0, 1024)
        self.memory.load(0, data)
        self.cpu.jamp(0)
        self.cpu.execute()
        

#Client Code: Uses the Facade instead of calling subsystem objects directly.
computer = Facade()
computer.start()

"""  
Benefits of the Facade pattern:
1.Simplifies the interface for a complex subsystem
2.Decouples the client from the subsystem
3.Promotes loose coupling between subsystems and clients
4.Provides a context-specific interface

Common use cases:
1.Providing a simple interface to a complex system
2.Structuring a system into layers
3.Reducing dependencies of outside code on the inner workings of a library

"""