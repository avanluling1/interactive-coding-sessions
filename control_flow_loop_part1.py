# if statements are about defining when or whether a block of code will run
# loops are about defining how many times a block of code runs
# it's about doing the same operation multiple times
# we are going to learn about two types of loops today

# 1. While loops
# contains a while keyword, followed by a logical statement, followed by a colon:
# inside, you have a code block again
# you have to give it some indication to stop
# or else it might run forever

count = 0
while count < 5:
    count = count + 1 # a variable that enters the condition is changing
    print(count)

# the skill: TRACING a loop
# understanding what is happening at each iteration
# and how many times the loop is going to run 

# iteration #, count
# first, 1
# second, 2
# third, 3
# fourth, 4

# second related skill, how many times a loop will run: 
# this isn't particularly interesting
# more realistic: 

user_input = ""
while user_input == "":
    user_input = input("Please type something:")
    print("The user typed: " + user_input)

# another example: a to-do list
# before that - a trick

age = 25
name = 'Abigail'
school = 'CU Boulder'
message = "My name is " + name + ", I am " + str(age) + " years old and I go to " + school
print(message)

# how to combine variables with text, but it's a PITA to write
# the gift of 'f strings'
better_message = f"My name is {name}, I am {age}, and I go to {school}"
print(better_message)

# back to loops
to_dos = ['walk the dog', 'mow the lawn','take out the trash','do the dishes']
while len(to_dos) != 0:
    item = to_dos.pop()
    print(f"I'm doing this: {item}. I still have to do: {to_dos}")

# let's try tracing this loop
# iteration #, item, to_dos:
# first iteration, 'do the dishes', ['walk the dog', 'mow the lawn','take out the trash']
# second iteration, 'take out the trash', ['walk the dog', 'mow the lawn']
# third iteration, 'mow the lawn', ['walk the dog]
# fourth iteration, 'walk the dog', []

# another common gotcha
# make sure to redefine the list, because all the popping made it empty

# the second type of loop that exists in Python are FOR LOOPS.
list_of_numbers = [1,2,3,4,5]
for i in list_of_numbers:
    print(i)

# anatomy of a for loop: 
# it starts with for
# immediately after for is a variable name
# it can be anything
# here it is i, but I could call number, n , x , a ... whatever
# this variable is called the step variable, it will take a different value at each loop
# then the keywork in
# then an iterable: any collection of items

list_of_numbers = [1,2,3,4,5]
for i in list_of_numbers:
    print(i)
# the for loop ITERATES over the ELEMENTS of the ITERABLE 
# storing each ELEMENT into the STEP VARIABLE at each loop. 

# let's consider a slightly more complex for loop:
# we have a list of numbers, and we want to print their sqaure:
list_of_numbers = [2,3,4,5]
for number in list_of_numbers:
    square = number ** 2
    print(f"The square of {number} is {square}")
# trace that loop before we run it:
# iteration #, number, square
# first iteration, 2, 4
# second iteration, 3, 9
# third iteration, 4, 16
# fourth iteration, 5, 25

# let's ramp up the complexity
# we have printed all the squares of these numbers
# but they haven't been stored anywhere
# it would be good to save them somewhere

list_of_numbers = [2,3,4,5]
list_of_squares = []
for number in list_of_numbers:
    square = number ** 2
    list_of_squares.append(square)
    print(f"The square of {number} is {square}, and our list of squares is now: {list_of_squares}")

# iteration #, number, square, list_of_squares
# first iteration, 2, 4, [4]
# second iteration, 3, 9, [4,9]
# third, 4, 16, [4,9,16]
# fifth, 5, 25 [4,9,16,25]

print(list_of_squares)

# let's practice two other for loops
# let's write one that can calculate the SUM of all numbers in a list
numbers_to_sum = [4,8,15,16,23,42]
total = 0 # initialize a total to zero
for number in numbers_to_sum:
    total = total + number
print(total)

# let's do the same for getting the maximum value in a list: 
numbers = [-3,5,7,-12,9,31]

from math import inf
maximum = -inf
for x in numbers:
    if (x > maximum):
        maximum = x
    print(f"The current item is {x}. The new maximum is {maximum}")
print(maximum == max(numbers))