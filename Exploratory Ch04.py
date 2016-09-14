# Exploratory CH04
# Follow the instructions to gain a better fluency with coding in Python.


#Instantiate two variables and assign values of 10 and 20 to them. Call them n1 and n2.
n1 = 10
n2 = 20

#Instantiate a third variable that is the sum of the first two. Call it n3.
n3 = 30
#Print n3.
print(n3)

#Concatenate and print n1 and n2 so that it reads '1020'.

#Use a temporary variable and correctly swap n1 and n2. Uncomment the line below.
print (str(n1) + str(n2))

print("n1 is now: " + str(n2))
print("n2 is now: " + str(n1))


#Write code that prompts the user for their first name, then their last name.
#Use appropriate variable names.
firstname = input('What is your first name?')
lastname = input('What is your last name?')

#Print the user's name in the form "lastName, firstName" 
print (lastname,',', firstname)


#Use a print statement to state the type of '2.72' and another for 'c'
print (type(2.72))
print (type('c'))

#Use an import statement and then print the square root of 4 to the 5th power.
import math
print(math.sqrt(4)**5)


#What does Python do if you try to evaluate the square root of -25? Show this.
#import math
#print (math.sqrt(-25))
#says math domain error

#Round down 4.9. Print the result.
import math
print (math.floor(4.9))

#Round up 6.2.   Print the result.
import math
print (math.ceil(6.2))


#Round 4.99 to the nearest integer.  Print the result.
print (round(4.99))

#Print the absolute value of -43.
print (abs(-43))