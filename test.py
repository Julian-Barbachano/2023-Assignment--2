class Product:
   print("Welcome to Programming Principles Sample Product Inventory")
   def __init__(self, c, n, p, m, s, e):
        self.code=c
        self.name=n
        self.price=p
        self.manufac=m
        self.stock=s
        self.emu=e

   def display(self):
       print("******Programing Principles Sample Stock Statement*****")
       print("Product Code: ", self.code)
       print("Product Name: ", self.name)
       print("Sale Price: ", self.price)
       print("Manufacture Cost: ", self.manufac)
       print("Monthly Production: ", self.emu, "(Approx.)")
    



