class Customer:

    def __init__(self,name):
        self.name = name

def greet(customer):
    print(id(customer))

    customer.name="Abc"
    print(customer.name)

cust = Customer("Ankita")
print(id(cust))

greet(cust)

print(cust.name)
  
