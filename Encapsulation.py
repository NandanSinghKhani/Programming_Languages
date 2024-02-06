class Atm:

    # constructor
    #special/magic/dunder methods

    # instance variable
    def __init__(self):
        
        self.__pin=" "
        self.__balance=0

        self.__menu()

    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin Changed")
        else:
            print("Not allowed")
        
    def __menu(self):       #method can be hide by using double underscore(__)
        user_input=input("""
                                Hello, how would you like to  proceed?
		1. Enter 1 to create pin.
		2. Enter 2 to deposit
		3. Enter 3 to withdraw
		4. Enter 4 to check balance
		5. Enter 5 to exit
""")
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.__pin = input("Enter your pin")
        print("Pin is set successfully")

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            self.__balance = self.__balance + amount
            print("Deposit successful")
        else:
            print("Invalid Pin")
                         
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount < self.__balance:
                self.__balance = self.balance - amount
                print("Operation successfully")
            else:
                print("insufficient funds")
        else:
            print("Invalid pin")
	
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid Pin")
            
