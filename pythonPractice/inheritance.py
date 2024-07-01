# #Inheritance : when one class(child/derived) derives the properties & methods of another class(parent/base) .

# class Car:
#     # -->> start()
#     # -->> stop()
#     # -->> color() 


# class ToyotaCar(Car):

class Car:
    @staticmethod
    def start():
        print("car started ..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car): ## inheritance  childClassName(parentClassName)
     def __init__(self, brand):
        self.brand=brand 

class Fortuner(ToyotaCar):
    def __init__(self, type): ## type can be diesel , petrol , electrical Car
        self.type=type

# car1=ToyotaCar('fortuner')
# car2=ToyotaCar("prius")

# print(car1.name)
# car1.start()

car1=Fortuner("diesel")
car1.start()