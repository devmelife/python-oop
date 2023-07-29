class Item:
    def __init__(self,name:str,price:float,quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self) :
        return  f"the item is {self.name} the price is {self.price} the quantity is {self.quantity}"
    def calculate_total_price(self):
        return self.price * self.quantity



item1 = Item("Phone", 500.2,2)
item2 = Item("Laptop", 1000, 2)

print(item1.calculate_total_price())
