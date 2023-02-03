class Emp:
    
    Emp_no=0
    def __init__(self ,fname,lname,salary):
          self.first_name=fname
          self.last_name=lname
          self.salary=salary
          Emp.Emp_no+=1 #for counting employees

    def increse(self):
        self.salary=int(self.salary*Emp.inc)   
    @classmethod    
    def change_increse(cls ,amount):
        cls.inc=amount
    @classmethod
    def from_str(cls,string): #class methosd as constructor
        fname,lname,salary=string.split('-')    
        return cls(fname,lname,salary)
    @staticmethod # static function
    def is_open(day):
        if day=='sunday':
            return 'holiday'
        else:
            return 'working day'        



kabir=Emp('kabir','morgan',70000)
print(Emp.is_open('monday'))
raju=Emp('raju','rashtogi',800000)
neha=Emp.from_str('neha-kannaujia-568888')
print(neha.first_name)
Emp.change_increse(6)
kabir.increse()
print(kabir.salary)
