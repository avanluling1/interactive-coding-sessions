# talk about collections
# collections are different ways of storing things into a single variable
# up until now, when you were assigning content to variables
# you were assigning a single thing: for instance
a = "hello"
b = 3.14

# now we are going to learn how to handle assigning multiple values to a single variable
# we are going to cover two kinds of collections today. The first kind is lists:

my_empty_list = [] # lists use two square brackets
# this is a list:
type(my_empty_list) # new type of object! int, str, float, bool, Decimal, list! 

# lists are what are called ORDERED collections of items
# you can use it to store a sequence of other elements:

my_favorite_numbers = [1,2,3,4,5] # you enter elements in the lists by adding them 
# between square brackets, one at a time, separated by commas
# lists can also contain strings
my_favorite_colors = ['red','blue','green']
# floats too!
my_favorite_floats = [3.14, 2.718, 1.1618]
my_favorite_bools = [False, True, False] #note that lists can contain
# repeated elemnts! they do not have to be unique! 

# you can also put different things in a list:
my_mixed_list = [False, 3.14, "Abigail", 1, True]

# you can even put lists inside a list
my_list_of_lists = [[1,2], ["hello",2], [False, 3.14]]

# you can really put anything you want inside a list.

# in python, a list is an object
# meaning, lists are going to have methods

# Let's see what exists inside a list.
my_favorite_colors.append #used for adding several elements to a list
print(my_favorite_colors.append("purple"))
# when you run the append method on a list, it does not return anything
# that's unlike what happens when you run a method on a string
# it returns the transformed string
my_name = "abigail"
print(my_name.upper())

print(my_favorite_colors) #success

print(my_name) #returns the original content because we did not perform a mutation

#LISTS ARE MUTABLE

# when we ran a method on a list, we saw a mutation
# it changed the original list
my_favorite_colors.append('purple')
print(my_favorite_colors) # every time you run append

a = my_favorite_colors.pop()

# because lists are ordered, we can check what is located where
# this is called INDEXING

my_favorite_numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
# to get the element located at a given INDEX in the list
# use [i], where i is the INDEX of the element that we want to get

print(my_favorite_numbers[0])

print(my_favorite_numbers[-2]) # moves from the far right (last number)

# That's called INDEXING: how we can grab a single element from a list
# now let's get more ambitious - how do we grab multiple
# uses SLICING
# slicing my_list[start:stop:step]
# start: where to begin
# stop: where to stop (index excluded)
# step: how many items are we skipping

print(my_favorite_numbers[0:5:1]) #grabs all the elements between index 0 and index 5
# excluding five, don't skip any
my_favorite_numbers[1:4:1]
my_favorite_numbers[0:6:2] # all numbers between zero and six (exclusive)
# skip every other number

# you can omit some of these arguments when you slice!!!
my_favorite_numbers[0:5] # step defaults to 1 when omitted
my_favorite_numbers[:6:1] # start defaults to 0 when omitted
my_favorite_numbers[::1]
my_favorite_numbers[::]

my_favorite_cities = ['Boulder','Paris']
lucas_favorite_cities = my_favorite_cities
print(my_favorite_cities)
print(lucas_favorite_cities)

#now, I'm going to visit Barcelona
my_favorite_cities.append('Barcelona')
print(my_favorite_cities)
# lucas now visits milan, and loves it! 
lucas_favorite_cities.append('Milan')
print(lucas_favorite_cities)

# in writing this: lucas_favorite_cities = my_favorite_cities
# I said Lucas and my favorite cities are defined by the same list 
# now, let's re-do the same exercise with a small change

my_favorite_cities = ['Boulder','Paris']
lucas_favorite_cities = my_favorite_cities[::] # this small change creates a copy of the list
# instead of matching them to each other
# can also do my_favorite_cities.copy()
print(my_favorite_cities)
print(lucas_favorite_cities)

# now, I'm going to visit Barcelona
# and it's great
my_favorite_cities.append('Barcelona')
print(my_favorite_cities)
# lucas now visits milan, and loves it! 
lucas_favorite_cities.append('Milan')
print(lucas_favorite_cities)

# back to our main topic: 
my_name = 'abigail'
print(my_name[1:4]) # you can index and slice strings!!!!! 

# since lists are mutable, you can do more than reading their content
# with indexing and slicing

my_favorite_colors # where do you find blue
my_favorite_colors[1] # how do you replace it?
my_favorite_colors[1] = 'pink' #place pink at the position 1
# replace what was there
print(my_favorite_colors)

# to add something in the middle of the list
# insert()
my_favorite_colors.insert(1, 'gold')
print(my_favorite_colors) # also works for pop

# final thing: we can also swap multiple values at the same time
my_favorite_colors[0:2] # we have a list of two elements
# if we want we can substitute two other elements
my_favorite_colors[0:2] = ['yellow','orange']
print(my_favorite_colors)
# what if the length of the sequence that you are trying to substitute does not match? 
# the length of the OG? 
my_favorite_colors[0:2] = ['black']
print(my_favorite_colors) # you can replace to values with one
# lists are MUTABLE!!!!

# there is one final thing
my_name = 'Abigail'
my_name[0] = 'X' # this will not work
# strings cannot be mutated

# another type of collection is called a Dictionary
# a dictionary is a collection of key-value pairs
# there are key ('words') that have values ('definitions') much like a real 
# word dictionary

# let me show you the syntax to create a dictionary:
my_friends_age = {"Nick": 40,
                  "Sam": 35,
                  "Juan": 37} # curly brackets, and inside, you put key:value pairs,
# separated by commas
# unlike lists, dictionaries are not ordered. They simply match values to keys. 

# the values in a dictionary can be of different kinds:
my_information = {
    "name" : "Abigail",
    "age" : 25,
    "hobbies" : ['skiing', 'birdwatching', 'ukulele']
}
# for the keys, there are more restrictions
# they are typically str, but sometimes int
# they must be unique
# they must be immutable objects
my_friends_age['Nick']

my_information['hobbies']

# dictionaries, much like lists, are mutable
# meaning we can reach into them and update a value

my_friends_age["Nick"] = 41
my_friends_age
my_friends_age["Alice"] = 56
my_friends_age

# dictionaries are also objects, meaning they have methods:
# two useful methods. 
# let's say we're not sure if a dictionary has a key
# when we try to index with that key, we might get an error like:
my_friends_age["Nico"] # KEY ERROR
# errors aren't great because they stop your code.
# instead we can use what is called a safe method called 'get()'
my_friends_age.get("Nico") #if they key exists, it returns the value.
# if it doesn't, it retunrs None

# if you want to delete a key from a dictionary
my_friends_age.pop('Sam') # pop for a list takes a numerical index
# for a dict, it takes a key
my_friends_age.values() # prints all of the values that exist:
my_friends_age.items() # prints all the key-value pairs

# final topic on dictionaries
# remember how I said that values can be anything
# values can be dictionaries themselves
# this is a very common data structure to represent users

my_friends_info = {
    # master dictionary: the keys are going to be usernames
    # the values are going to be dictionaries containing information about the users
    "Nick" : {
        "age": 41,
        "hobbies" : ['basketball', 'cooking'],
        "city": "Boulder"
    },
    "Sam" : {
        "age" : 35,
        "hobbies" : ['hiking','painting'],
        'city' : "Chicago"
    }
}

# how do we use a more complex data structure like this
# how would you get all of Nick's infos? 

my_friends_info["Nick"] # what is the type of this object?
# it's a dictionary!
# let's double check

nicks_info = my_friends_info["Nick"]
type(nicks_info)
# so, if this is a dictionary
# how do we get Nick's age

my_friends_info["Nick"]['age']

# let's do another practice
# you know that you have a friend called Sam
# you're not sure if you have information about his hobbies
my_friends_info.get("Sam").get("hobbies") # this looks for Sam as if we don't know he exists
my_friends_info['Sam'].get('hobbies') # this is what we use when we know Sam exists

# Nick recently picked up an exciting hobby: Sourdough baking! 
# Can you add this hobby to Nick's list of hobbies

my_friends_info['Nick'].get('hobbies').append('Sourdough baking')
my_friends_info['Nick'].get('hobbies')

# can be
my_friends_info['Nick']['hobbies'].append('sourdough baking')
# you can use numerous brackets to dive deeper into a dictionary

# can you add two hobbies in a row
my_friends_info['Nick']['hobbies'].append('sourdough baking').append('sourdough baking')
# because append returns none, you can't append off of none
my_friends_info['Nick']['hobbies'].append('sourdough baking', 'skydiving')
# this would work