# A program that manages an inventory of products
# inventory keeps track of the id of each product
# the product quantity and price can be changed


class Product:
    def __init__(self, price, name, id_product, quantity):
        self.price = price
        self.name = name
        self.id = id_product
        self.quantity = quantity

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    # update price
    def update_price(self, new_price):
        if new_price <= 0 or new_price <= self.price:
            print(
                "Invalid price. Price must not be less than zero or be the same as the current price"
            )
        else:
            self.price = new_price

    # update quantity
    def update_quantity(self, new_quantity, increment):
        if increment == "add":
            self.quantity += new_quantity
        elif increment == "subtract" and (self.quantity - new_quantity) >= 0:
            self.quantity -= new_quantity
        else:
            print("Can't reduce any further.")

    # View product id, name of product, price, and quantity
    def view_product(self):
        print(
            "Product ID: "
            + str(self.id)
            + ", Name: "
            + self.name
            + ", Quantity: "
            + ", Price: "
            + str(self.price)
            + str(self.quantity)
        )


class Inventory:
    def __init__(self):
        self.inventory_list = []

    def add_prod(self, pID):
        self.inventory_list.append(pID)

    def remove(self, pID):
        if pID in self.inventory_list:
            self.inventory_list.remove(pID)
        else:
            print("Product does not exist in inventory")

    def get_list(self):
        return self.inventory_list


apple = Product(0.25, "apple", 1, 25)
print(apple.get_price())
apple.update_price(0.50)
print(apple.get_price())
apple.view_product()

inventory = Inventory()
inventory.add_prod(1)
print(inventory.get_list())
