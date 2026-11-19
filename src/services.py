from interfaces import CalculateTaxesInterface, RegisterInterface

class EuropeTax(CalculateTaxesInterface):
    def __init__(self):
        self._country_tax = {"ES": 0.21, "FR":0.20, "DE": 0.19, "PT": 0.23}

    def apply_tax(self, subtotal: float, country_code: str) -> float:
        tax = self._country_tax.get(country_code.upper(), 0.21)
        return subtotal * (1 + tax)

class WithoutTaxes(CalculateTaxesInterface):
    def apply_tax(self, subtotal: float, country_code: str) -> float:
        return subtotal

class RegisterConsole(RegisterInterface):
    def log_operation(self, order_details: dict):
        print("NEW ORDER REGISTERED")
        for k, v in order_details.items():
            print(f"{k}: {v}")

class RegisterMemory(RegisterInterface):
    def __init__(self):
        self._historial = []
    
    def log_operation(self, order_details: dict):
        self._historial.append(order_details)

    @property
    def historial(self):
        return self._historial