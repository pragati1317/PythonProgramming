#List in python
marks=[87, 63,43,53,18,39,98] #marks[0], marks[1], marks[2]
## Hytrogenous type of data in list .
student =["Karan", 85, "Delhi"] #student[0],student[1]
student[0]='Arjun' #allowed in python

print(len(student)) 

# List Slicing (Similar to String Slicing)

# list_name[starting_idx : ending_idx] #ending idx is not included 

# print(marks[1:])
# print(marks)
# print(marks[-3:-1])

# # List Methods
# Mylist=[2,1,3,1]
# Mylist.append(4)
# Mylist.sort()

# Mylist.sort(reverse=True)
# print(Mylist)

# Mylist.reverse()
# Mylist.insert(6, 7)
# print(Mylist)

# Mylist.remove(1) #remove first occurrence of element
# print(Mylist)
# Mylist.pop(4) #removes element at idx
# print(Mylist)

#Tuples in Python { immutable sequences of values.}

tup=(87, 64,33, 95,76) # tup[0] , tup[1]..
# tup[0]=43 #Not allowed in Python

tup1=()
tup2=(1,)
tup3=(1, 2,3)

# tuple Methods
tup=(2, 1,3,1,3) ## But redefine the same variable of tuple
print(tup.index(3)) #returns index of first occurence 
print(tup.count(1))

lst=["c", "d","s", "A", "B", "A", "B", "A"]
lst.sort(reverse=True) 
print(lst)