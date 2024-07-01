# del keyword  : Used to delete object properties or object itself

# del s1.name ## delete the property of Object
# del s1 ## delete the object

class Student:
    def __init__(self, name):
        self.name=name

s1=Student('shradha')

print(s1.name)
del s1
# print(s1) ## deleted { error}

##private(like) attributes & method ---> implemented By using _(2 underscore) just infront of the variableName and MethodName

class Account: 
    def __init__(self, acc_no, acc_pass):
        self.acc_no =acc_no
        # self.acc_pass=acc_pass ## Public Attribute Method
        self.__acc_pass=acc_pass ## Now it is Private Attribute.

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
# print(acc1.__acc_pass) ## { Give error , As This Attribute is Private.}
acc1.reset_pass()

## Private Function Example 

class Person:
    __name="anonymous"

    def __hello(self):
        print('hello person! ', self.__name) ## These private Function used for Internal working ..

    def welcome(self):
        self.__hello()

p1=Person()
# print(p1.__name) # It will give errorr.

p1.welcome()