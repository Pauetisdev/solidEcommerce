from abc import ABC, abstractmethod

class ShippableInterface(ABC):
    """Products that require shipping and incur delivery costs."""
    @abstractmethod
    def ship_cost(self, quantity: int)-> float:
        pass

class GiftWrapInterface(ABC):
    """Products that support gift wrapping for a fixed fee."""
    @abstractmethod
    def add_wrap(self):
        pass

class CalculateTaxesInterface(ABC):
    """Tax calculation strategies based on destination country."""
    @abstractmethod
    def apply_tax(self, subtotal: float, country_code: str) -> float:
        pass

class RegisterInterface(ABC):
    """Order logging and persistence backends"""
    @abstractmethod
    def log_operation(self, order_details: dict):
        pass