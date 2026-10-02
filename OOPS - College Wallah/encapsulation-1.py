class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self.__balance=balance
        
    
    #getter
    def getBalance(self):
        return self.__balance
    
    
    def deposit(self, amount_deposited):
        self.__balance=amount_deposited
        print("Amount is added successfully: ", self.__balance)
        
        
    #withdraw
    def Withdraw(self, amount_to_withdraw):
        if amount_to_withdraw>self.__balance:
            print("Insuffient Balance")
            return
        self.__balance-=amount_to_withdraw
        print("Amount is withdraw successfully: Updated Balance: ", self.__balance)
        
        
acc1= BankAccount("Pavan", 100000)
print(acc1.name)
acc1.name= "Kalyan"
print(acc1.name)
#print(acc1.__balance)
print(acc1.getBalance())
acc1.deposit(5000)
print(acc1.getBalance())
acc1.Withdraw(1000)
acc1.Withdraw(900000)





