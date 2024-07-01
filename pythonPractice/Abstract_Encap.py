#Abstraction 
# ---> Hiding the implementation detais of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True ## hiding this Main Work to user (Abstraction)
        print("car started..")

car1=Car()
car1.start()

#3 Encapsulation
##Wrapping data and functions into a single unit (object).

class Account:
    def __init__(self , bal, acc):
        self.balance=bal
        self.account_no=acc
    
    def get_balance(self):
        return self.balance

    #debit method 
    def debit(self,amount):
        self.balance-=amount
        print("Rs.", amount , "was debited")
        print("total balance =", self.get_balance())

    def credit(self , amount):
        self.balance+=amount
        print('Rs.', amount, "was credited")
        print("total balance =", self.get_balance())

acc1=Account(10000, 134345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(456);
acc1.credit(567);
