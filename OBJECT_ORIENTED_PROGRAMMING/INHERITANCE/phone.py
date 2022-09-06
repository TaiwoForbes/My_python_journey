from item import Item
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