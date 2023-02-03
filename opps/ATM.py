class ATM:
    def __init__(self):
        self.__pin=''
        self.__balance=0
        self.__menu()
    def __menu(self):
        user_input=input("""
         hello how would you like tpo proceed
         *. Enter 1 to create pin
         *. Enter 2 to deposit
         *. Enter 3 to withdraw
         *. Enter 4 to check banance
         *. Enter 5 to exit
        """)  
        if(user_input=='1'):
            self.create_pin()
        elif user_input=='2':
            self.deposit()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.balance_check()
        else:
            print("bye") 

    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("pin changed")

    def create_pin(self):
        self.__pin=input("Enter your pin")
        print("pin has been updated successfully")  

    def deposit(self):
        temp=input("Please enter your pin ")
        if(temp==self.__pin):
            amount=int(input("Enter your amount"))
            self.__balance=self.__balance+amount
            print("Amount has been deposited successfully in your account")
        else:
            print("invalid pin")    

    def withdraw(self):
        temp=input("Please enter your pin ")
        if(temp==self.__pin):
            amount=int(input("Enter your amount"))
            if amount<self.__balance:

                self.__balance=self.__balance-amount
                print("Please collect your money")
            else:
                print('insufficient fund')
        else:
            print('invalid pin')  



    def balance_check(self):
        temp=input("Please enter your pin ")
        if(temp==self.__pin):
            print(self.__balance)
        else:
            print("invalid pin")                     

