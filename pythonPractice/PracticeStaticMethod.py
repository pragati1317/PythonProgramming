# static Method don't use Self Parameter.(work at class level)
        #     class (static) method
       #    /       \
      #    /         \
     #  obj1(self)       obj2(self) method     
          

class Student: 
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    
    # def hello(): 
    #     print("hello")  ## this helo() function will give error , as self is mandatory in class functions

# for static Method use decorator (@staticmethod)

    @staticmethod
    def college():
        print("sgsits indore")

s1=Student("tony stark",[99, 98, 97])
# s1.college()
Student.college() #3 static Method Don't  depend on the object instance of the class .

# what is Decorators ? 
## It take function input , and give back a function by changing the behaviour of it