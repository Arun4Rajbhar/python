# def add(a,b):
#     return a+b
# print(add(23,89))    

class pop:
    def __init__(self,a,b):
        print("inside constructor")
        self.first=a
        self.second=b

        print(self.add())
      


    def add(self):
        return self.first+self.second
            



obj=pop(78,56)



