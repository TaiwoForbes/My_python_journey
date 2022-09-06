class Item:
    def __init__(self,name:str,price:float,quantity:float): # The init method is caled first before the instance created
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

item = Item(1,100,10)
print(item.calculate_total_price())