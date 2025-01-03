'''# Define a function to calculate the greatest common divisor of 2 numbers.
def gcd(x, y):
    # Initialize gcd to 1.
    gcd = 1
    
    # check if y is a divisor of x (x is divisible by y).
    if x % y == 0:
        return y
    # Iterate from half of y down to 1.
    for k in range(int(x), 0, -1):
        # Check if both x and y are dicisible by k.
        if x % k == 0 and y % k == 0:
            #update the gdc to the current value of k and exit the loop.
            gcd = k
            break
        # Return the calculated GCD value.
    return gcd
x=int(input("Enter 1st integer value: "))
y=int(input("Enter 2nd Integer value: "))

#print("GCD of", x, "and" ,y ,": ", gcd(x, y))
print(f"GCD of {x} and {y} is :", gcd(x, y)) '''

'''# Define a function 'lcm' that calculate the least common multiple fo two number 'x' and 'y'.
def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y
    
    # Use a 'while' loop to find the LCM
    while True:
        # Check if 'z' is divisible by both 'x' and 'y' with no remainder.
        if (z % x == 0) and (z % y == 0):
            # If both conditions are met, 'z' is the LCM, so store it in 'lcm' and break the loop.
            lcm = z
            break
        # If the conditions are not met, increment 'z' and continue checking.
        z = z + 1
    # Return the calculated LCM
    return lcm
# Enter two integer value to fing LCM
x=int(input("Enter 1st Integer value: "))
y=int(input("Enter 2nd Integer Value: "))

print(f"lcm of {x} and {y} is :", lcm(x,y))'''

'''def sum_three(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum
x=int(input("Enter as Integer value of x: "))
y=int(input("Enter as Integer value of y: "))
z=int(input("Enter as Integer value of z: "))

print(f"Sum of {x} {y} and {z} is: ",sum_three(x, y, z))'''

'''def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum
x=int(input("Enter 1st integer value: "))
y=int(input("Enter 2nd integer value: "))
print(sum(x, y))'''

'''def test(x, y):
    if x == y or abs(x - y) == 5 or (x + y) == 5:
        return True
    else:
        return False
a=int(input("Enter Integer Value: "))
b=int(input("Enter Integer Value: "))
print(test(a, b))'''

'''def add_number(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Input must be integer"
    return a + b
print(add_number('2',20))'''

'''def personal_details(x, y, z):
    print(f"Name: {x}\nAge: {y}\nAddress: {z}")
name=input("Enter user Name: ")
age=input("Enter User age: ")
address=input("Enter User address: ")
personal_details(name, age, address)'''

'''def msolve(a, b):
    result=a*a + 2*a*b + y*y
    print(f"({a} + {b})^2 = {result}")
x=int(input("Enter 1st Numerical value: "))
y=int(input("Enter 2nd Numerical value: "))
msolve(x, y)'''

'''amt=int(input("Enter Principle Amount: "))
intr=float(input("Enter Inerest rate: "))
yrs=int(input("Enter no of years: "))
comp_value = amt*((1+ (0.01* intr))**yrs)
print(round(comp_value, 5))'''

'''import os.path
print(os.path.isfile('main.py'))'''

# Open the file 'main.py' for reading.
my_file = open('Hello.py')
try:
   # Close the file.
   my_file.close()
   # Print "File found!" if the file was successfully closed.
   print("File found!")
except FileNotFoundError:
   # Print "File not found!" if a FileNotFoundError occurs when closing the file.
   print("File not found!")
    