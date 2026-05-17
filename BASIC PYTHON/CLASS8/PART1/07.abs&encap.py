
#.abstraction

'''Abstraction ek concept hai jisme hum sirf zaruri cheezein dikhate hain aur
unnecessary details ko chhupaate hain.
Simple words mein: Complex cheez ko simple banao — 
sirf woh dikhao jo user ko chahiye, baaki sab andar chhupa do.
Example — Real Life:
Car chalate waqt tum sirf steering, accelerator, aur brake use karte ho.
Engine ke andar kya ho raha hai — pistons, fuel injection, combustion — 
yeh sab hidden hai. Yahi abstraction hai.'''

class Car:
    @staticmethod
    def car_st():
        clutch = True
        acc = True
        brk = False
        print("car started")
    @staticmethod
    def car_stop():
        clutch = False
        acc = False
        brk = False
        print("car stop")
c1 = Car()
c1.car_st()
c1.car_stop()

#.encaptulation
#: data sedhe nahi milta methods se milta hain 
#: means encaptulation means safety

''' ATM Machine
-----------
Tumhara paisa andar band hai  →  Private data (__balance)
Tum seedha paisa nahi chhu sakte  →  Direct access blocked
ATM ke buttons use karte ho  →  Methods (withdraw, deposit)
ATM check karta hai pehle  →  Validation
Tab paisa milta hai  →  Controlled access '''