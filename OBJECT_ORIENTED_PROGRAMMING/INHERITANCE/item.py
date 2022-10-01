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
        self.__name = name
        self.__price = price
        self.quantity = quantity
    
    

    

        # Action to perform
        Item.all.append(self)
        print("An instance is created {} {} {}".format(name,price,quantity))

    @property
    def name(self):
        return self.__name # Note: using a single underscore will not prevent the attribute outside the class
                          # But using double underscore will prevent the usage of the attribute outside the class
    @property
    def price(self):
        return self.__price

    @name.setter # Setter is used when we still want to make ammendment to our private/property attribute
    def name(self,value):
        if len(value) > 10:
            raise Exception ("String is too big")
        else:
            self.__name = value

    def increment(self,value):
        self.price = self.__price + (self.__price * value) 

    def apply_discount(self):
        self.price = self.__price * self.pay_rate


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
    # Property Decorator : Read-Only Atrribute
   
        
        
    def calculate_total_price(self):
        return self.price * self.quantity