#let's recreate a variable or two
my_integer = 10
my_str = 'Hello World'

type(my_integer)
type(my_str) #the answer returned by these functions is CLASS
#everything in python is an object

#what is stored inside an object?
my_str.upper #a method is a like a function - it needs to be called
# we put parentheses after

my_str.upper() #returning a copy means that the original is unchanged
my_str.lower()
my_str.endswith('!')
my_str.endswith('orld')
#methods are a way of pairing functions to specific types of objects

# some objects have other things than methods: Properties
# Properties are information about the objects that was created

my_integer.denominator #white wrenches are properties of the objects
my_integer.numerator #properties don't need parentheses - they are only meant to be read 
#and don't perform any action
#if something doesn't require a calculation to be given to you
# and does not do anything, probably a property
#icon verifies type

#let's check a few more methods that exist on a string
my_name = 'abigail vanLuling'
my_name.capitalize()
print(my_name.title())
print(my_name.count('n')) #counts occurrences of argument in string
print(my_name.replace('n','X'))
print(my_name.replace('vanLuling','Smith'))
#methods are a natural way of acting on an object and encapsulating functions that
# are relevant to the type of object

n_chars = len(my_name)
print(n_chars) #len is a function, it is not called from within the object, it stands alone
my_upper_name = my_name.upper() #this is a method, you're calling it from within the object
#methods use the dot to call
#in general Python doesn't implement a method if a straight forward function exists

#what will this line do?
print(my_name.lower) #without parentheses, python has no idea what to do 
my_age = 25
print(my_age.numerator) #these are properties I can read directly
#properties have the wrench and methods have the purple box

greeting = "hello welcome to class"
print(greeting.upper())
print(greeting) #most methods return a new value - think of them as a machine
#that is copying
#the original and modifies it
#the original is not every changed
# technical jargon: the methods do not mutate the original objects

user_input = "     abigail.vanluling@colorado.edu       "
#check that the entered email is a .edu
trim_input = user_input.strip()
print(trim_input)
good_solution = trim_input.endswith('.edu')
print(good_solution)
better_solution = user_input.strip().endswith('edu') #bucket methods within each other
#methods read left to right to visualize impacts
print(better_solution)
#comp check
is_this_true = user_input.strip().upper().endswith('.edu')
print(is_this_true)

#comp check two
user_input.strip().endswith('.edu').upper() #upper method doesn't exist for bool, so it 
#follow a method that creates a bool
# segue into some of the errors that can pop up: 
user_input.shout() #attribute error: when you attempt to reach for a method or property
# that does not exist on an object

my_age.denominator #won't work because you're attmepting to call and attribute
#like it's a method

#there are more than four different types of objects in Python
# how are objects of different types created: 
my_int = 10
my_str = 'something with quotes'
# to create other objects you need to call an object factory
# here, we will work with an object called Decimal that allows you to create 
# decimal numbers with exact representations
# no floating point errors

from decimal import Decimal
a = Decimal('.1')
print(type(a))
b = Decimal('.2')
# there are more than four object types and once they exist you can see 
# all the associated methods
print(a+b)

my_name = 'Abigail'
my_name.count()

passed = 8 > 5

test = [0,1,2,3,4,5,6]
x = test.pop()
print(x)
print(test)


test1 = [0,1,2,3,4,5,6]
x1 = test1.append(7)
print(x1)
print(test1)

test.pop()