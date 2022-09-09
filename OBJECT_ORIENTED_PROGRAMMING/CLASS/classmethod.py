import csv

'''A class attribute belong to the class itself but also can e shared in the instance attribute itself '''
class Item:
    # This sets a default value of the class attribute
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
        

    @classmethod # The class method use the class reference as the first argument
    def instantiate_from_csv(cls):
        with open('class.csv', 'r') as f:
            reader = csv.DictReader(f) # This will read the csv content as a dictionary
            items = list(reader) # This converts the reader into a list

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    def __repr__(self):
        # The repr prints the strings representation of an object
        return f"Item('{self.name}',{self.price},{self.quantity})"
        
        
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

# Notice that we are calling the class attribute Item and this is possible by using the @classmethod decorator
print(Item.instantiate_from_csv())
print(Item.all)