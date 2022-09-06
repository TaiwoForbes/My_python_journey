'''A class attribute belong to the class itself but also can e shared in the instance attribute itself '''
class Item:
    # This sets a default value to the class attribute
    pay_rate = 0.8 # Pay rate after 20% discount
    def __init__(self,name:str,price:float,quantity:float): # The init method is called immediately the instance created
        #Run validationto received arguments
        assert price >= 0 , f"Price {price} must be greater than or equal to zero"
        assert quantity >= 0 , f"Quantity {quantity} must be greater than or equal to zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        print("An instance is created {} {} {}".format(name,price,quantity))
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone",100,10)
print(item1.calculate_total_price())
# Assessing the class attribute
print(Item.pay_rate) # This from the class attribute itself
print(item1.pay_rate) # This from the instance attribute,assesssing the class attribute
print(Item.__dict__) # This is used to check all the attribute that belongs to a specific object
print(item1.__dict__)
print()
item1.apply_discount()
print(item1.price)
print(item1.calculate_total_price())
print()

item2 = Item("Laptop", 100,10)
item2.pay_rate = 0.6 # Changing the value of pay_rate which has a default value in the class attribute from instance level
item2.apply_discount()
print(item2.price)
