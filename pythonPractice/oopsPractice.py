## Oops in Python
## To map with real world scenarios , we started using objects in code.It is called object oriented programming 

## class & object in Python

#creating class
class Student : 
    # name = "karan Kumar";
    college_name = "SGSITS , Indore"

    ## default constructors 
    def __init__(self):
        pass ## pass used for future code.

    ## Parameter Constructors.    
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        print("adding new student in Database..")

#creating object (instance, instance of class )

# s1=Student() 
# print(s1.name) #using default name value

class Car: 
    color="blue"
    brand="mercedes"

## __init_function == constructor 
# All classes have a function called_init_(), which is always executed when the object is being initated.

#creating class                  #creating object
                                     
# class Student:                     |   s1 =student ("karan")
    # def __inti__(self , fullname): |   print(s1.name)
        # self.name =fullname        |

## self is a argument which target the new Object that we are Creating.So using self targeting itself .

s1=Student('karan', 74)
print(s1.name, s1.marks, s1.college_name)

s2=Student('arjun', 97)
print(s2.name, s2.marks, s2.college_name)

## inplace of self parameter , we can give another name for that parameter

## class & instance Attributes (class.attr , obj.attr)

# ---> collegeName ---> class attribute , as Same for every student.(class Attribute required less Memory ,as It is static variable)