# casefold() # this function is used to convert the string into lowercase . 
# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case

# Indexing 
# Apna_college 12 length string.
str="Apna_College" 
# str[0]='B' #not allowed { Python Strings are Immutable.}
new_str = 'B' + str[1:] 
print(new_str) # it is the Write way.

##Slicing  : (Accessing parts of a string) 
# str[starting_idx : ending_idx] ##ending idx is not included

#Slicing 
# Accesing parts of a string 

# str[starting_idx : ending_idx] #ending idx is not included
# str='ApnaCollege'
# str[1:4] is "pna"
# str[:4] is same as str[0:4]
# str[1:] is same as str[1: len(str)]

str1="Apple"
print(str1[-3:-1])
str.capitalize( ) #capitalizes 1st char

str.find( "college" ) #returns 1st index of 1st occurrence
# str.replace( old, new ) #replaces all occurrences of old with new
str.endswith("ge") #returns true if string ends with substr
str.count("na") #counts the occurrence of substr in string