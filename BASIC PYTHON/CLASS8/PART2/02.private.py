'''#. Private attributes aur methods 
woh hote hain jo sirf apni class ke andar access aur use kiye 
ja sakte hain class ke bahar ya kisi aur class se 
directly access nahi hote.
Inhe `__` (double underscore) se banate hain.'''

class Account:
    def __init__(self,password,acc_no):
        self.__password = password
        self.acc_no = acc_no

    def reset_pass(self):
        print(self.__password)
    
a1 = Account("abc","xyz")
a1.reset_pass()
