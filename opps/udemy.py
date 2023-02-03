class User:
    def login(self):
        print("login")
    def register(self):
        print("register")

class student(User): #student is child class of user class
    def enroll(self):
        print("enroll")

    def reveiw(self):
        print("reveiw")         


s1=student()
s1.login()
s1.enroll()        
