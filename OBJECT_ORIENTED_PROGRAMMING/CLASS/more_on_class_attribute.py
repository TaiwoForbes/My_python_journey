'''A class attribute belong to the class itself but also can e shared in the instance attribute itself '''
class Item:
    # This sets a default value to the class attribute
    pay_rate = 0.8 # Pay rate after 20% discount
    all = []
    def __init__(self,name:str,price:float,quantity:float): # The init method is called immediately the instance created
        #Run validationto received arguments
        assert price >= 0 , f"Price {price} must be greater than or equal to zero"
        assert quantity >= 0 , f"Quantity {quantity} must be greater than or equal to zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to perform
        Item.all.append(self)
       
    
    def __repr__(self):
        # The repr prints the strings representation of an object
        return f"Item('{self.name}',{self.price},{self.quantity})"
        
        
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone",100,10)
item2 = Item("Laptops",100,10)
item3 = Item("Cable",100,10)
item4 = Item("Mouse",100,10)
item5 = Item("Keyboard",100,10)

print(Item.all)

for item in item1.all:
    print(item1.price)


