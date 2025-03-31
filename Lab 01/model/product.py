class Product:
    def __init__(self, product_id=None, name=None, date_supplied=None, quantity_in_stock=0, unit_price=0.0):
        self.product_id = product_id
        self.name = name
        self.date_supplied = date_supplied
        self.quantity_in_stock = quantity_in_stock
        self.unit_price = unit_price

    def to_dict(self):
        return {
            "productId": self.product_id,
            "name": self.name,
            "dateSupplied": self.date_supplied,
            "quantityInStock": self.quantity_in_stock,
            "unitPrice": self.unit_price
        }
