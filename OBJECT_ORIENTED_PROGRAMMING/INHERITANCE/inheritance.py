import csv

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
        print("An instance is created {} {} {}".format(name,price,quantity))

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
    # Staticmethod is use when you want to check if a method has a logical connection to the class, example to check integer and so on
    @staticmethod # The object/instance is not received as the first argument, meaning is takes argument like a normal function does
    def is_integer(num):
        if isinstance(num,float):
            # Counts the float that are point zero as an integer
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        # The repr prints the strings representation of an object
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
        
        
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

class Phone(Item):
    
    # When using the init method in the child class, it is expect to use a certain functions called SUPER
    # SUPER allows us to have full access to the attribute of the parent class
    def __init__(self,name:str,price:float,quantity:float, broken_phones = 0): # The init method is called immediately the instance created
        # Run validationto received arguments
        super().__init__(

            name,price,quantity
        )
       
        assert broken_phones >= 0 , f"Broken_phones {broken_phones} must be greater than or equal to zero"

        # Assign to self object
        
        self.broken_phones = broken_phones
        # Action to execute
        

        
       


phone1 = Phone("Nokia", 800,2,1)
print(phone1.calculate_total_price())
print(Phone.all)
item1 = Item("Tecno",800,2)
print(Item.all)
