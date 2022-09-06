class Characteristics:
    species = "Homoserpien"
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return self.name
    def rename(self,rename):
        self.name = rename
        print("Now my name is {}".format(rename))

Taiwo = Characteristics("Taiwo")
print(Taiwo)
Taiwo.species = "Nerds"
print(Taiwo.species)
Taiwo.rename("Shola")