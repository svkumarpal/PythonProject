# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:04:47 2024

@author: svkum
"""
day=input("Enter Day: ")
amount=int(input("Enter Amount: "))

if day.lower() == "sunday" and amount >=8000: #lower() will convert in lower case
    discount = (amount*50)/100
    amount=(amount - discount)
    print("After 50% discount final amount to pay: ", int(amount))
elif day.lower() == "sunday" and amount >=6000:
    discount = (amount*35)/100
    amount=(amount - discount)
    print("After 35% discount final amount to pay: ", int(amount))
elif day.lower() == "sunday" and amount >=4000:
    discount = (amount*25)/100
    amount=(amount - discount)
    print("After 25% discount final amount to pay: ", int(amount))
else:
    print("Without Discount final ammount to pay: ",int(amount))