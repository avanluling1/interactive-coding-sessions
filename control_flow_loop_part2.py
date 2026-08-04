# advanced topics in loooops! 

# let's start with the concept of iterables.
# we have seen that we can loop over lists with for loops:

for i in [1,2,3,4]:
    print(i)

# we can loop with for over ANYTHING that is iterable:
# like a string!

for l in "hello world": #the l in this case is not the letter l, it's a variable to designate each part
    # of a list or string
    print(l)

# we know that strings are iterable
# because we can also slice them

# what else can we iterate on? 
my_info = {"name" : 'abigail',
           "age" : 25,
           "city" : 'boulder'}

for key in my_info:
    value = my_info[key]
    print(value)

# it would be better if we could get both the key and th evalue 
# when iterating over a dictionary (right?)
# there is a way

# .... but first a small detour:
my_fruits = ['banana', 'apple', 'mango']
first_fruit, second_fruit, third_fruit = ['banana','apple','mango']
# this is called unpacking (we're putting things into variables)
name, age, city = "Abigail", 25, "Boulder" # making three variables at the same time
# that's acceptable

# let's return to our dictionary:
my_info.items() # use this to make my info into a "list" of sorts (not actually a list)

for (key, value) in my_info.items():
    print(f"The key is {key}, and associated value {value}")

# let's revisit the example of looping on my name:
my_name = 'Abigail'
for letter in my_name:
    print(letter)

# I would like to know the index of each letter in my name
# when you face an iteration issue - enumerate()
# how it works: 

for (index, letter) in enumerate(my_name): # returns the index AND the element, index is first no matter what you call it
    print(f"The letter at position {index} is {letter}")

# the only thing that you need to do is: 
# replace iterable by enumerate(iterable)
# replace step_variable by (index, step_variable)

# second power tool
a_list_of_food = ['pickle','pepper','peach']
a_list_of_tastes = ['sour','spicy','sweet']

# you can iterate over two lists (or multiple) in parallel.
# all you have to do first is zip them.
for (food, taste) in zip(a_list_of_food, a_list_of_tastes):
    print(f"A {food} tastes {taste}")

# what if we also had color? 
a_list_of_colors = ['green', 'red', 'orange']

for (food, taste, color) in zip(a_list_of_food, a_list_of_tastes, a_list_of_colors):
    print(f"A {food} is {color} and tastes {taste}")

# zip is a way of combining iterables

# the first thing to cover (08/04) is a small utility to create lists
# of numbers that we can loop on

# let's say I wanted to print all the squares between 0 and 1000
# the way we have done this so far, was something like: 
list_of_numbers = [0,1,2,3,4,1000]
# we can make a large ilst of numbers using range
# in its basic form, range works like: 
for i in range (1000):
    print(i ** 2)
# it takes one argument: stop: the value at which you will stop
# always stops one value before
# you can also give two other arguments: start and step 
for i in range(3,10,2): #SLICING! 
    print(i)
# they work in the same way for range, except that they create an iterable
# rather than slicing the values in an existing iterable
for i in range(5,30,5):
    print(i)

# now for something slightly more complicated
# let's say we want to generate a list of all the squares
# of the numbers 1-9
# we'll do that using a for loop first.
squares = []
for i in range(1,10):
    square = (i**2)
    squares.append(square)
print(squares)
# we built a list one element at a time
# using a for loop
# when you have to build a list (or any iterable) from another list (or another iterable)
# you will often encounter something called a LIST COMPREHENSION 
# it's simply a for loop written in a more concise way

sqaures = [i **2 for i in range(10)]
# a list comprehension starts with square brackets: 
# after all, we're building a list
# then comes the loop, FOR STEP_VARIABLE IN ITERABLE.
print(squares)

first_name = 'abigail'
whats_this = [x.upper() for x in first_name]

# you can add another "bell" to a list comprehension, an optional part
# you can filter certain elements

# we want to get the squares of all the numbers between 0 and 9 but ONLY
# if the square is less than 30.
small_squares = [i ** 2 for i in range(0,10) if (i **2) < 30]
# same list comprehension as before
# except we have an if statement. that conditions whether an element
# will be added to the list or not
# if at a given iteration the condition is false
# it's not added
print(small_squares)

# let's say you have a folder full of mess. you're working with a disorganized 
# colleague called Quentin

folder_content = ['data.csv', 'report.pdf', 'summary.csv', 'image.png', 'notes.txt', 'data2.csv', 'archive.zip']

# what I want: filter out all the elements that are not csv files
# reminder, you can chekc if a file name ends with csv by using .endswith("csv")

folder_content = [i for i in folder_content if i.endswith(".csv")] #alwyas expression, then assignment
print(folder_content)