# Answer: 1
print("Twinkle, twinkle, little star,\n     How i wonder what you are!\n         Up above the world so high,\n         Like a diomand in the sky.\nTwinkle, twinkle, little star,\n     How i wonder what you are")


# Answer: 2
import sys
print (sys.version)

# Answer: 3
from datetime import datetime as dt
now = dt.now()
print ("current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Answer: 4
import math
r = input("Input the radius of the circle : ")
pi = math.pi
area= pi*float(r)**2
print ("The area of the circle with radius " + str(r) + " is \n" + str(area))

# Answer: 5
fname=input("Input your first name : ")
lname=input("Input your last name : ")
print( lname + " " + fname)

# Answer: 6
num1 = input("Enter first number : ")
num2 = input("Enter second nmber : ")
sum =float(num1) + float(num2)
print(sum)



