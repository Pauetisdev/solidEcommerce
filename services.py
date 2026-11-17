from interfaces import CalculateTaxesInterface

class EuropeTax(CalculateTaxesInterface):
    def __init__(self):
        self._country_tax = {"ES": 0.21, "FR":0.20, "DE": 0.19, "PT": 0.23}

    def apply_tax(self, subtotal: float, country_code: str) -> float:
        tax = self._country_tax.get(country_code.upper(), 0,21)
        return subtotal * (1 + tax)

class WithoutTaxes(CalculateTaxesInterface):
    def apply_tax(self, subtotal: float, country_code: str) -> float:
        return subtotal

