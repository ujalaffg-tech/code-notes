
'''Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance.'''
class Account:
    
    def __init__(self,balance,acc):
        self.balance = balance
        self.acc = acc

    def debit(self,ammount):
        self.balance-=ammount
        print("rs",ammount,"was debited")
        print("total balance =",self.balance)
    
    def credit(self,ammount):
        self.balance+=ammount
        print("rs",ammount,"was credited")
        print("total balance =",self.balance)
    
    def check_bal(self):
        print("avillable balance =",self.balance)

a1 = Account(10000,"abc")
a1.debit(1000)
a1.credit(6000)
a1.debit(7000)
a1.check_bal()