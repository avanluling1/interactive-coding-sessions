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