class phone:  #use of super()  keyword
    def __init__(self,prize,brand,camera):
        print('inside phone constructor')
        self.prize=prize
        self.brand=brand
        self.camera=camera
         
   


class smartphone(phone):

    def __init__(self, prize, brand, camera,os,ram):
        print('start point')
        super().__init__(prize, brand, camera)
        self.os=os
        self.ram=ram
        print('inside smartphone constructor')



p1=smartphone(30000,'samsung','sony','android','4gb')
print(p1.brand)
print(p1.os)
      