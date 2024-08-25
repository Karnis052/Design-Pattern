"""  
The Iterator design pattern is a behavioral pattern that provides a way to access
elements of an aggregate object sequentially without exposing its underlying representation. 

Key components:

1. Iterator: Interface defining methods for traversing a collection
2. Concrete Iterator: Implements the Iterator interface
3. Aggregate: Interface defining method for creating an Iterator
4. Concrete Aggregate: Implements the Aggregate interface

"""


from collections.abc import Iterator, Iterable
# Concrete Iterator:  class that implements the iteration logic.
class ListIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index =0
    
    def __next__(self):
        if self._index < len(self._collection):
            value = self._collection[self._index]
            self._index +=1
            return value
        raise StopIteration

# Concrete Aggregate (Iterable): Implements the Aggregate interfac
class NumberCollection(Iterable):
    def __init__(self):
        self.numbers = []
    
    def addNumber(self, number):
        self.numbers.append(number)
    
    def __iter__(self) -> Iterator:
        return ListIterator(self.numbers)
    
#Client Code    
collection = NumberCollection()
collection.addNumber(1)
collection.addNumber(2)
collection.addNumber(3)

for number in collection:
    print(number)
    
    
""" 
Advantage:

1. Decoupling: The client does not need to know about the internal structure of the collection.
2. Single Responsibility: Separates the traversal logic from the collection's data structure.
3. Allows for different traversal algorithms

"""