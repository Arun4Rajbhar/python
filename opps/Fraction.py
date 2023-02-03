class fraction:
    def __init__(self ,n,d):
        self.nume=n
        self.deno=d
    def __str__(self):
        return "{}/{}".format(self.nume,self.deno)

    def __add__(self,other):
        temp_nume=self.nume*other.deno+self.deno*other.nume
        temo_deno=self.deno*other.deno
        return "{}/{}".format(temp_nume,temo_deno)

    def __sub__(self,other):
        temp_nume=self.nume*other.deno-self.deno*other.nume
        temo_deno=self.deno*other.deno
        return "{}/{}".format(temp_nume,temo_deno)  

    def __mul__(self,other):
        temp_nume=self.nume*other.deno*self.deno*other.nume
        temo_deno=self.deno*other.deno
        return "{}/{}".format(temp_nume,temo_deno)   

    def __truediv__(self,other):
        temp_nume=self.nume*other.deno+self.deno*other.nume
        temo_deno=self.deno*other.deno
        return "{}/{}".format(temp_nume,temo_deno)      

