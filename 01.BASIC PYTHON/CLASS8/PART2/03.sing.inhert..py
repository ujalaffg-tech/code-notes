
#. single enheritance
class Car:

    @staticmethod
    def start():
        print("car started ")
    @staticmethod
    def stop():
        print("car stoped")

class Toyota(Car):
    def __init__(self,name):
        self.name = name

t1 = Toyota("fortuner")
t1.start()


