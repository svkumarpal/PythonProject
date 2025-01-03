# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:30:18 2024

@author: svkum
"""
#x=input()
#x=input("Enter a Number: ")
#x=input("Enter a number:")
#y=input("Enter a number:")
#z=x+y
#print(z)
# there is 2 typ2 of casting 1- Imlicit and 2- Direct
# casting refers to changing an variable of one data type into another. 
# The compiler will automatically change one type of data into another 
# if it makes sense. For instance, if you assign an integer value to a 
# floating-point variable, the compiler will convert the int to a float.
# Python does not allow implicet casting
# to check type of value user type()
# x = input("Enter a number: ") #input fun always return in String type. 
# To resolve this issue  we used to used type casting, 
# In text file all data always be in string format hence nedd data casting here as well
# type(x),x - tocheck data type
x=int(input("Enter a Number:"))
y=int(input("Enter a Number:"))
z=x+y
type(z),z
print(z)
# only digits [0-9] value can be convert through type casting
