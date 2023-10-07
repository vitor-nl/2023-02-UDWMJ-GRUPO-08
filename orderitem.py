import order
import product

class Orderitem(order.Order, product.Product):
    def __init__(self, quantity, unitary_price):
        self.quantity = quantity
        self.unitary_price = unitary_price
        
        