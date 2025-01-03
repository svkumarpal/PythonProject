# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:51:26 2024

@author: svkum
"""

#nested if condition
#day=input("Enter Day: ")
#amount=int(input("Enter Amount: "))

#if day == "sunday" and amount >=5000:
 #   discount = (amount*10)/100
 #   amount=(amount - discount)
 #   print("After 10% discount final amount to pay: ", amount)
#else:
 #   print("Without Discount final ammount to pay: ",amount)
    
day=input("Enter Day: ")
amount=int(input("Enter Amount: "))

if day.lower() == "sunday" and amount >=5000: #lower() will convert in lower case
    discount = (amount*10)/100
    amount=(amount - discount)
    print("After 10% discount final amount to pay: ", amount)
else:
    print("Without Discount final ammount to pay: ",amount)