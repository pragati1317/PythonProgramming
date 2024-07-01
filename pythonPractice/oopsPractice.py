## Oops in Python
## To map with real world scenarios , we started using objects in code.It is called object oriented programming 

## class & object in Python

#creating class
class Student : 
    # name = "karan Kumar";
    college_name = "SGSITS , Indore"
    name="anonymous" # class attr 

    ## default constructors 
    def __init__(self):
        pass ## pass used for fut ure code.

    ## Parameter Constructors.    
    def __init__(self, name, marks):
        self.name=name # obj attr > class attr (precedance )
        self.marks=marks
        print("adding new student in Database..")

    def welcome(self): ## self parameter is mandatory
        print('welcome student,' ,self.name)
    
    def get_marks(self):
        return self.marks
    
    def average(self): 
        n=(int)(len(self.marks) )
        sum=0
        for x in self.marks:
            sum+=x
        val=sum/n
        print("hi", self.name , "yout avg score is:", val)
        return val
#creating object (instance, instance of class )

# s1=Student() 
# print(s1.name) #using default name value

class Car: 
    color="blue"
    brand="mercedes"

## __init_function == constructor 
# All classes have a function called_init_(), which is always executed when the object is being initated.

#creating class                      | #creating object
                                     
# class Student:                     |   s1 =student ("karan")
    # def __inti__(self , fullname): |   print(s1.name)
        # self.name =fullname        |

## self is a argument which target the new Object that we are Creating.So using self targeting itself .

s1=Student('karan', 74)
print(s1.name, s1.marks, s1.college_name)

s2=Student('arjun', [84, 47,67,59,98])
print(s2.name, s2.marks, s2.college_name)
s2.average()

## inplace of self parameter , we can give another name for that parameter

## class & instance Attributes (class.attr , obj.attr)

# ---> collegeName ---> class attribute , as Same for every student.(class Attribute required less Memory ,as It is static variable)
