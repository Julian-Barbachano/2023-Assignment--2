import random
class Product:
   
   def __init__(self, c, n, s, p, m, e, ):
        self.code=int(c)
        self.name=str(n)
        self.stock=int(s)
        self.price=int(p)
        self.manufac=int(m)
        self.emu=int(e)
        

   def display(self):
       print("******Programing Principles Sample Stock Statement*****")
       print("Product Code: ", self.code)
       print("Product Name: ", self.name)
       print("Sale Price: ", self.price)
       print("Manufacture Cost: ", self.manufac)
       print("Monthly Production: ", self.emu, "(Approx.)")

   #def months(self):
       
       #intr = random.randint(-10,10)
       
       #print("Month 1: ")
       #print("-  Manufactured: ", self.emu)
       #print("-  Sold: ", self.emu + )
       #print("-  Stock: ", self.emu + )
     

print("Welcome to Programming Principles Sample Product Inventory")
prod_instance = Product(input("Please enter the Product Code: "), input("Please enter the Product Name: "), 
                        input("Please enter the Current Stock: "), input("Please enter the Product Sale Price: "),
                          input("Please enter the Product Manufacture Cost: "), (input("Please enter estimated monthly production: ")))

prod_instance.display()

prod_instance.months()
