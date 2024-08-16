"""  
The Strategy design pattern is a behavioral design pattern that enables selecting
an algorithm's behavior at runtime. 
"""

from abc import ABC, abstractmethod

# Context: Uses the strategy
class ShoppingCard:
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def addItem(self, item, price):
        self.items.append((item, price))
    def setPaymentStrategy(self, payment_strategy):
        self.payment_strategy = payment_strategy
        
    def checkOut(self):
        total = sum(price for _, price in self.items)
        
        if self.payment_strategy:
            self.payment_strategy.pay(total)
        else:
            print("No payment method is selected")

#Strategy interface: Defines common interface for all strategies
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, total):
        pass
    
#Concrete strategies: Implement the strategy interfac
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, name):
        self.card_number = card_number
        self.name = name
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card {self.card_number}")

#Concrete strategies: Implement the strategy interfac
class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal account {self.email}")
 
#Concrete strategies: Implement the strategy interfac       
class BankTransferPayment(PaymentStrategy):
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def pay(self, amount):
        print(f"Paid ${amount} using Bank Transfer from account {self.bank_account}")
        
#Client Code
card = ShoppingCard()
card.addItem("Laptop", 10000)
card.addItem("Mouse", 400)

# Pay with Credit Card
# Dependency Injection: The payment strategy is injected into the cart.
card.setPaymentStrategy(CreditCardPayment("1234-5678-9012-3456", "Karnis"))

card.checkOut()

# Pay with PayPal
#Dependency Injection: The payment strategy is injected into the cart.
card.setPaymentStrategy(PayPalPayment("karnis@example.com"))

card.checkOut()

# Pay with Bank Transfer
# Dependency Injection: The payment strategy is injected into the cart.
card.setPaymentStrategy(BankTransferPayment("DE89 3704 0044 0532 0130 00"))
card.checkOut()


"""  
1. A ShoppingCart class that acts as the context, using the selected payment strategy to process payments.
2. A PaymentStrategy abstract base class defining the interface for all payment strategies.
3. Concrete strategy classes (CreditCardPayment, PayPalPayment, BankTransferPayment) implementing specific payment methods.

Benefits:
Allows switching algorithms at runtime
Promotes open/closed principle
Separates algorithm implementation from its use

Common use cases:
Sorting algorithms
Payment processing methods
Compression algorithms
"""