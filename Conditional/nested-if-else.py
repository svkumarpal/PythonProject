# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:45:36 2024

@author: svkum
"""
# if bot
x=int(input("Enter A number: "))
y=int(input("Enter A number: "))

# check if both value is not eawual
if x!= y:
    if x>y:
        print(x,"is greatet than",y)
    else:
        print(y,"is greated than x",x)
else:
    print(y,"are equal to",x)