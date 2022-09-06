class Item:
    def calculate_total_price(self,x,y):
        return x * y

item = Item() # Instance of an oblect
item.name = "Pnone" # istance attribute
item.quantity = 20
item.price = 100
print(item.calculate_total_price(item.price,item.quantity))
