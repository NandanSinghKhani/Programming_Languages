class Customer:

    def __init__(self,name,age):
        self.name= name
        self.age =age

    def intro(self):
        print("I am",self.name,"and I am",self.age)

c1 = Customer("abc",34)
c2 = Customer("xyz",55)

L = [c1,c2]

for i in L:
    print(i.name, i.age)

for j in L:
    i.intro()
    
