# before we begin working on arrays, we are going to import a library
import numpy as np # will always see this abbrev as np
import math
# you reach into a library using the dot notation
print(math.pi)
print(math.sqrt(9))

# let's create our first array together:

my_array = np.array([1,2,3,4,5]) # we are using the function
# with a single argument: [1,2,3,4,5]
print(my_array)
# looks a lot like a list
print(my_array[0])
print(my_array[0:3])

# difference 1: arrays can only contian elements of the same type.
my_list = ["Quentin", False, 42]
print(type(my_list[0]))

# now let's try to create an array with the same contents
my_array = np.array(['Abiagil', False, 42])
print(my_array)

# all of the elements changed to strings
# why? because arrays require everything to be one type
# when we create an array with multiple types, they all get converted
# to one single compatible type
# because arrays only contain a single type, they have what is called a datatype

print(my_array.dtype)

int_array = np.array([1, 2, 3])
float_array = np.array([3.14, 2.76, 1.12])
bool_array = np.array([False, True, True])
print(int_array.dtype)
print(float_array.dtype)
# arrays have a dtype, that conditions what lives inside of them.

# second difference between lists and arrays:
# arrays have a fixed size, something called a shape.

my_list = [1,2,3,4,5]
my_list.append(6)
my_list
my_list.pop(0)
my_list
# the length of a list changes

my_array = np.array([1,2,3,4,5])
my_array.append(6)
my_array.pop(0)
# you cannot change the length of an array
# you cannot add or remove elements from the array.
# what you can do is create a new array, with additional elements
my_bigger_array = np.append(my_array, 6)
my_bigger_array
my_array # the original array has not changed

# knowing the single type of an array allows you to do much more than you can do
# with a list that can contain any amount of information

# let's see what we can do with arrays that we can not do with lists:

# suppose we sell five products. I'm going to write down their prices
# and quantities sold:

prices = [9,19,4,14,24]
quantities = [120,75,300,50,40]
# p and 1 for 5 diff products

# forgetting about arrays: 
# I would like you to calculate, for each of the five items
# the total revenue (price times quant)

revenues = []
for (p,q) in zip(prices, quantities):
    r = p *q 
    revenues.append(r)
print(revenues)

# this results in a list containing the revenues for the five items

arr_prices = np.array(prices)
arr_quantities = np.array(quantities)
arr_revenues = arr_prices * arr_quantities
print(arr_revenues)
# python knows you want the element wise product of these two arrays
# this operation is much simpler to write and is much faster
# this is because python knows what is going on 

# numpy implements "vectorized operations" that allow computers to work much faster
# let's see another example showing how much nicer it is to work with arrays

# sales for five products in two months: 
sales_jan = np.array([120, 75, 300, 50, 40])
sales_feb = np.array([110, 60, 330, 80, 25])
feb2jan = sales_feb - sales_jan
print(feb2jan)

# by how much did the sales grow between january and february
growth = (sales_feb/sales_jan)
print(growth)

whats_this = sales_feb == sales_jan
print(whats_this)
# arrays look at the element, not holistically 
whats_this_again = sales_feb >= sales_jan
print(whats_this_again)

# what else? np contains a bunh of functions that can be applied to arrays:
np.sqrt(sales_jan)
np.exp(sales_jan)

sales_jan.mean()

# what can go wrong when working with arrays?
five_prices = np.array([1,2,3,4,5])
four_quants = np.array([1,2,3,4])
four_quants * five_prices # to be added, multiplied, divided, compared, etc
# arrays need to have compatible shapes
print(four_quants.shape)
print(five_prices.shape)
str_arr = np.array(['A', 'B', 'C', 'D'])
str_arr + four_quants

# indexing with arrays
arr_prices = np.array([5,10,15,20,25])
print(arr_prices[0]) # you can use indexing to read values and replace
arr_prices[0] = 20
print(arr_prices)

# we can also use slicing to access values in arrays
print(arr_prices[0:3])

# these two behaviors are common to lists and arrays
# with arrays you can do two more things: 

#1: boolean indexing or masking
arr_prices = np.array([7, 14, 21, 20, 25])
mask = [False, False, True, True, False]
arr_prices[mask] # using square brackets and the mask as an index
# all the elements that had a false in front of them were omitted
# only the elements that had a True in front of them were returned by the indexing

# example 1:
arr_q = np.array([10, 20, -5, -2, 4, 10]) # this array contains errors (negative sales quants)
mask2 = arr_q < 0 # this will check how the array compares to a given number
arr_q[mask2]

# can we fix these errors using the mask somehow? 
arr_q[mask2] = 0

# bonus one liner
arr_q[arr_q < 0] = 0

bakery_visits = np.array([0,15,12,8,9,0,5])
# these are the visits to a bakery, Monday through Sunday

# (i) how many visits did the bakery get per day on average?
bakery_visits.mean()
# (ii) are there are any days where the bakery did not get any visits? show them.
mask_zero_visits = (bakery_visits == 0)
bakery_visits[mask_zero_visits]
# (iii) excluding the days where the bakery did not get any visits, how many visitors did it get?
bakery_visits[bakery_visits > 0].mean()

# second thing is much simpler (that you can do with arrays and not lists)
# also has a cool name: "Fancy" Indexing

arr_words = np.array(["The, Quick","Brown", "Fox"])
# fancing indexing is just giving a list of indices that you want the value of

desired_indices = [0,1,3]
arr_words[desired_indices]

# you can also repeat positions
desired_indices = [0,1,3,0,1,2]
arr_words[desired_indices]

# what's the use of fancy indexing?
# most common use is randomly selecting rows in a dataset

# exactly like indexing, except you can use a list of numbers rather than just one
# you can also skip the variable definition:
arr_words[[0,1,0,1,3]] # two brackets, first to say I'm indexing, second to say here's the list