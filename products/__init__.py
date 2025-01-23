from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict):
        """Load product data from a dictionary."""
        return Product(
            data.get('id', 0),
            data.get('name', ''),
            data.get('description', ''),
            data.get('cost', 0.0),
            data.get('qty', 0)
        )


def list_products() -> list[Product]:
    """Fetches and returns all products as a list of Product objects."""
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product | None:
    """Fetches a product by its ID."""
    product_data = dao.get_product(product_id)
    return Product.load(product_data) if product_data else None


def add_product(product: dict):
    """Adds a new product to the database."""
    required_keys = {'id', 'name', 'description', 'cost', 'qty'}
    if not required_keys.issubset(product.keys()):
        raise ValueError(f"Product must have the following keys: {', '.join(required_keys)}")
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Updates the quantity of a product."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    if not dao.get_product(product_id):
        raise ValueError(f"Product with ID {product_id} does not exist")
    dao.update_qty(product_id, qty)