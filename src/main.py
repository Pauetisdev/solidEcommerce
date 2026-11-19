from products import Product, PhysicalProduct, DigitalProduct, PerishableProduct
from services import EuropeTax, WithoutTaxes, RegisterConsole, RegisterMemory
from manager import OrderManager

def build_catalog() -> dict[str, Product]:
    gpu = PhysicalProduct("G-001", "Nvidia's GPU", 2600, 5)
    wip_access = DigitalProduct("WIP-001", "WIP Platform Access", 2700, 10)
    psalm = PerishableProduct("PSALM-LNF", "Fresh Salmon", 17, 80, 2)
    
    return {
        gpu.sku: gpu,
        wip_access.sku: wip_access,
        psalm.sku: psalm,
    }

def show_catalog(catalog: dict[str, Product]):
    print("\n--- PRODUCT CATALOG ---")
    for product in catalog.values():
        print(
            f"[{product.sku}] {product.name} | "
            f"Price: {product.unit_price:.2f} EUR | Stock: {product.stock}"
        )

def add_to_cart(catalog: dict[str, Product], cart: list[tuple[Product, int]]) -> None:
    while True:
        show_catalog(catalog)
        sku = input("\nEnter product SKU to add (or 'DONE' to return): ").strip().upper()

        if sku == "DONE":
            break

        if sku not in catalog:
            print(f"Error: SKU '{sku}' not found in catalog.")
            continue

        try:
            quantity = int(input("Enter quantity: ").strip())
            if quantity <= 0:
                print("Error: Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Error: Quantity must be a valid integer.")
            continue

        product = catalog[sku]
        cart.append((product, quantity)) # tuple
        print(f"Added {quantity}x '{product.name}' to cart.")

def checkout(cart: list[tuple[Product, int]], manager: OrderManager) -> dict:
    if not cart:
        print("\nYour cart is empty. Add products before checking out.")
        return

    country_code = input("\nEnter destination country code (ES, FR, DE, PT): ").strip().upper()
    gift_input = input("Wrap as a gift? (y/n): ").strip().lower()
    is_present = gift_input == "y"

    try:
        manager.process_order(cart, country_code, is_present)
        cart.clear()
        print("Order processed successfully!")
    except ValueError as error:
        print(f"\nOrder failed: {error}")


def main() -> None:
    catalog = build_catalog()
    cart: list[tuple[Product, int]] = []

    tax_service = EuropeTax()
    register_service = RegisterConsole()
    manager = OrderManager(tax_service, register_service)

    while True:
        print("\n=== E-COMMERCE ORDER ENGINE ===")
        print("1. View Catalog")
        print("2. Add Products to Cart")
        print("3. Checkout")
        print("4. Exit")

        option = input("Select an option: ").strip()

        match option:
            case "1":
                show_catalog(catalog)
            case "2":
                add_to_cart(catalog, cart)
            case "3":
                checkout(cart, manager)
            case "4":
                print("Exiting application...")
                break
            case _:
                print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()