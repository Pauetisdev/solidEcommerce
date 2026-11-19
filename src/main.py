from products import PhysicalProduct, DigitalProduct, PerishableProduct
from services import EuropeTax, WithoutTaxes, RegisterConsole, RegisterMemory
from manager import OrderManager

gpu = PhysicalProduct("G-001", "Nvidia's GPU" ,2600, 5)
wip_access = DigitalProduct("WIP-001", "WIP Platform Access", 2700, 10)
psalm = PerishableProduct("Psalm-LNF", "Fresh Psmal", 17, 80, 2)

europe_tax = EuropeTax()
register_console = RegisterConsole()

manager = OrderManager(europe_tax, register_console)

cart = [(gpu, 2), (wip_access, 1), (psalm, 1)]
try:
    manager.process_order(cart, "ES", True)
    print(gpu.stock)
except ValueError as e:
    print(e)

cart = [(gpu, 1), (wip_access, 25)]
try:
    manager.process_order(cart, "FR")
except:
    print(gpu.stock)


without_taxes = WithoutTaxes()
register_memory = RegisterMemory()

manager = OrderManager(without_taxes, register_memory)
cart = [(gpu, 2), (wip_access, 1), (psalm, 1)]
try:
    manager.process_order(cart, "ES", True)
    print(gpu.stock)
except ValueError as e:
    print(e)