#we have seen many functions already:
print('Hello World')
print(len('Hello'))
print(abs(-7))
print(str(3.14))
print(int('294'))
# what we're going to see to do is dissect what functions are doing and what they are
# a function is like a machine
# it typically takes inputs between 0 and many
# it is running commands, doing things, and most often it RETURNS
# something to the user
# you can think of most functions as a conveyer belt

# If I use the len function():
my_str = 'Hello world'
len_of_my_str = len(my_str) #takes a single argument, here a string
# returns to the user the length of that string.
print(len_of_my_str)
# a function that returns something is useful because it gives you something back
# that you can store into a variable and reuse for other purposes later

# not all functions are like that - not all functions are conveyer belts
# others are more like engines - they take inputs like gas and O2
# they do things, but they do not return anything to the user

print('Hello world') # every time this runs, it will print Hello world to the REPL
what_is_this = print('Hello world')
print(what_is_this) # this prints 'None'
# there is nothing in this variable (none type)
# a function like one that writes data to a file does "nothing"

# one last thing to know
# functions take arguments. we can supply the arguments in two ways
# 1. By Position
print(round(3.14,1)) # the first argument is the num to round, 2nd is the num of digits
# order matters
print(round(1,3.14)) #generates an error 
# the second way is to include what are called named arguments
print('A','B','C','D') #you gave the function arguments in sequence 
# and it will print them all 
# the print function also takes secret arguments that have default values
# meaning you don't specify, they already exist
print('A','B','C','D', sep='*')
print('A','B','C','D', sep='*', end='!')
# named arguments must always come last (otherwise error)

# you can use names to eliminate all ambiguity about positional arguments
round(number = 3.14, ndigits = 1) # you don't need the argument word, but with it things are less confusing
# this is the same thing as round(3.14,1)
# to know the name of the arguments, use the () in VSCode

# Let's practice writing our own functions now 
# We write functions when we want to have a list of actions that we can easily reuse in different places

# Create a function that can calculate a price increase
# when given a rate: 

# Define a function: 
def show_price_increase(base_price, rate_increase):
    #the body of your function is what will happen every time the function is called
    new_price = base_price * (1 + rate_increase)
    print(new_price)
    # we are now done, we press shift enter to define the function 

# now the function exists, we can call it 
show_price_increase(10,.1)
#what kind of function did we create
# conveyer belt or engine? engine because it's not giving us back anything, just printing a new price
new_price = show_price_increase(10,.2)
print(new_price) #prints none - our function is not returning anything

# Define a new function: 
def calculate_price_increase(base_price, rate_increase):
    #the body of your function is what will happen every time the function is called
    new_price = base_price * (1 + rate_increase)
    return new_price # return without parentheses is what the function delivers to the user 
    # we are now done, we press shift enter to define the function 

my_new_price = calculate_price_increase(5,.25)
print(my_new_price) # this time, there's an output, because we chose to return a variable
# whatever happens inside a function is lost after the function is done running
# if you want to get it back, ask the function to return it 

# one final thing with functions

def show_total(price, quantity):
    print("Starting to calculate the price...")
    total = price * quantity
    return total # engine or conveyer? conveyer because of the return
    print("Finished calculating the price") #this won't run because the function sees return and considers the work done

total = show_total(.99, 10)
print(total)