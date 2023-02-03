class Customer:  #aggrigation
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address


    def edit_profile(self,new_name,new_city,new_pincode,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pincode,new_state)    


class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state

    def change_address(self,new_city,new_pincode,new_state):
        self.city=new_city
        self.pincode=new_pincode
        self.state=new_pincode


add1=Address('mumbai',400701,'maharashtra')
cust1=Customer('rahul','male',add1)  

cust1.edit_profile('Rahul','chennai',400701,'bengluru')
print(cust1.address.pincode)
