class phone:  #use of super()  keyword
    def __init__(self,prize,brand,camera):
        print('inside phone constructor')
        self.prize=prize
        self.brand=brand
        self.camera=camera
         
    def buy(self):
        print('buying a phone')


class smartphone(phone):
    def buy(self):
        print('buying a smartphone')
        super().buy() # super keyword can be used to access parent's method and constructor only
        #if you have constructor in both child and parent class then child class can only invoke it's own constructor but if you want to invoke parent's contructor you can do it using super() keyword
p1=smartphone(30000,'samsung','sony')
p1.buy()        


