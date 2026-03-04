# variables
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

"""

# Simple examples of legal variables 
myvar = "Muntazer"
my_var = "Muntazer"
_my_var = "Muntazer"
myVar = "Muntazer"
MYVAR = "Muntazer"
myvar2 = "Muntazer"

print(myvar,my_var,myVar,MYVAR,myvar2)


# illegal variable names:
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""
# collections   to store the large amount of data

# list  []
cloud_students_list = ["Ali","Ahmad","Muntazer"]
print(cloud_students_list)
print(type(cloud_students_list))
#tuple   ()
cloud_students_tuple = ("Ali","Ahmad","Muntazer")
print(cloud_students_tuple)
print(type(cloud_students_tuple))
#dictionary   {}
student_dict = {
    "name":"Muntazer","age":21,"address":"Muzaffargarh"
}

print(student_dict)
print(type(student_dict))
#set   are the collection of identical methods
my_set = {"apple", "banana", "cherry","Banana","banana"}  # set ignore the dublicate items just write once
print(my_set)
print(type(my_set))

# important thing in set there is no index set are unstructured
# Example   print(my_set[0])   # ❌ ERROR

# If your goal is just to check whether a name exists in a set:
if "banana" in my_set:
    print("Found!")