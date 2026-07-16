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
my_integer.numerator #properties don't need parentheses - they are only meant to be read and don't perform any action
#if something doesn't require a calculation to be given to you
# and does not do anything, probably a property
#icon verifies type