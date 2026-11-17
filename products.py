from abc import ABC, abstractmethod
from statistics import quantiles

from interfaces import ShippableInterface, GiftWrapInterface

class Product(ABC):

    def __init__(self, sku: str, name: str, unit_price: float, stock: int):
        self._sku = sku
        self._name = name
        self.unit_price = unit_price
        self.stock = stock

    @property
    def sku(self) -> str:
        return self._sku

    @property
    def name(self)-> str:
        return self._name

    @property
    def unit_price(self) -> float:
        return self._unit_price

    @unit_price.setter
    def unit_price(self, price: float):
        if price < 0:
            raise ValueError("Price can not be negative")
        self._unit_price = price

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, new_stock: int):
        if new_stock < 0:
            raise ValueError("Stock can not be negative")
        self._stock = new_stock

    @abstractmethod
    def calculate(self, quantity: int) -> float:
        pass

class FisicProduct(Product, ShippableInterface, GiftWrapInterface):

    def calculate(self, quantity: int) -> float:
        return self.unit_price * quantity

    def ship_cost(self, quantitat: int)-> float:
        return 5.0 + (1.5 * quantitat)

    def add_wrap(self):
        return 3.50

class DigitalProduct(Product):

    def calculate(self, quantity: int) -> float:
        total_price = self.unit_price * quantity
        discount = 0.15
        if quantity >= 3:
            return total_price * (1 - discount)
        return total_price

class ProductePerible(Product, ShippableInterface): # Producte fresc

    def __init__(self, sku: str, name: str, unit_price: float, stock: int, caaducity_days: int):
        super().__init__(sku, name, unit_price, stock)
        self.__caducity_days = caaducity_days

    def calculate(self, quantity: int) -> float:
        total_price = self.unit_price * quantity
        discount = 0.30
        if self.__caducity_days <= 2:
            return total_price * (1- discount)
        return total_price

    def ship_cost(self, quantitat: int)-> float:
        return quantitat * 2.50