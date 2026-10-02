class BankAccount:
    def __init__(self, name, password):
        self.name=name
        self.__password= password 
        
    #setter
    def NewPassword(self, new_password):
        self.__password= new_password
        print("Passowrd Updated")
        
        
a1= BankAccount("Pavan", 12345)
print(a1.NewPassword(123456))

