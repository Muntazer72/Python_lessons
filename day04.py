#understanding functions and data types

# there are two types of funcitons 1  user defined 2  built in functions such as print() , type() and etc
# cexample of built in function
def sum(num1,num2):   #defining the function
    return num1+num2

x = sum(100,200)  # here function call
print(x)   # this is built in function


# another example of a function

def my_function():
  print("Hello from a function")
my_function()


# task example code of function
# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions, you would have to write the same calculation code repeatedly:
# Without functions - repetitive code:

print("Without functions - repetitive code:")
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# in case of using function farenheit to celsius 

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9
print("converting from farenheit to calscius")
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# from celsius to farenheit 
def celsius_to_farenheit(celsius):
   return (celsius*9/5)+32
print("converting from celscius to farenheit")

print(celsius_to_farenheit(77))
print(celsius_to_farenheit(95))
print(celsius_to_farenheit(50))