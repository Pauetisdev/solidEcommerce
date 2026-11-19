from abc import ABC, abstractmethod

class ShippableInterface(ABC):
    @abstractmethod
    def ship_cost(self, quantity: int)-> float:
        pass

class GiftWrapInterface(ABC): # Returns a fix sumplement
    @abstractmethod
    def add_wrap(self):
        pass

class CalculateTaxesInterface(ABC):
    @abstractmethod
    def apply_tax(self, subtotal: float, country_code: str) -> float:
        pass

class RegisterInterface(ABC):
    @abstractmethod
    def log_operation(self, order_details: dict):
        pass