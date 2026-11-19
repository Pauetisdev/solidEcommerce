from interfaces import CalculateTaxesInterface, RegisterInterface, ShippableInterface, GiftWrapInterface
from products import Product
class OrderManager:
    def __init__(self, taxes: CalculateTaxesInterface, log: RegisterInterface):
        self._taxes = taxes
        self._log = log

    def process_order(self, cart: list[tuple[Product, int]], country_code: str, is_present: bool = False ) -> dict:
        """Validate stock, calculate totals with taxes, update inventory, and log the order."""
        
        for product, qtt in cart:
            if product.stock < qtt:
                raise ValueError("There isn't enought stock")
        
        subtotal = 0.0
        skus_sell = []

        for product, qtt in cart:
            subtotal += product.calculate(qtt)

            if isinstance(product, ShippableInterface):
                subtotal += product.ship_cost(qtt)

            if is_present and isinstance(product, GiftWrapInterface):
                subtotal += product.add_wrap()

            product.stock -= qtt
            skus_sell.append(product.sku)

        net_import = self._taxes.apply_tax(subtotal, country_code)

        summary = {
            "skus": skus_sell,
            "country": country_code.upper(),
            "is_present" : is_present,
            "subtotal" : round(subtotal, 2),
            "total": round(net_import, 2)
        }

        self._log.log_operation(summary)
        return summary