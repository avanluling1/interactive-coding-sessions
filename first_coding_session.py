print("Hello World") #in our python file (also called Python script)
print("Hello Friends") #final way of running python code: Run a script in full 

#what are the big variables types in python 
this_string = "Abigail" #this is a string, this string will not return anything

this_float = 3.14 #this is a float
this_int = 12 #this is an int
this_bool = False #note case sensitivity 

#what can you do with variables? 
#only after running can you refer to the variables (python needs to know them)
print(this_string)
print(this_float)

#what else can you print?
print(this_string) #print variable
print("Hello") #you can print a literal
print(12) #you can print a literal number too
print(12+5) #you can print an expression
#SKILL: being able to trace the code - reconstruct the steps of a code
#an expression will be calculated first and then printed
# order code is written is not the order code is evaluated
#another example of expression
print(this_float + 5) #here we can trace the steps

#what is print()?
# print is a function. a function is a way of doing something in python
# functions are called using parentheses ()
# functions take a number of arguments (what goes inside the parentheses). some take zero, some take many

#how many arguments does print take?
#it can take one
print(this_float)
#it can take more
print(this_float, this_int, this_string)

#let's do some calculations!
print(2+3)
print(2*5)
print(2 + 3 * 5)
print((2+3)*5)

print(0.1+0.2) #will cause a floating point error, accuracy only to the 16th decimal point

print((0.1 + 0.2) == 0.3)

#to avoid floating errors, try rounding
my_rounded_sum = round(0.1 + 0.2, 1)
print(my_rounded_sum)
print((my_rounded_sum) == 0.3)

print(1<2)
print(1>2)
print(1>=2)
print(1<=2)
print(1!= 2)

#you can also create more complex comparisons
print(1 < 2) and (3 > 2)

condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False
print(condition_1 and condition_2)
print(condition_1 and condition_3)
#and requires all conditions to be true
print(condition_1 or condition_2)
print(condition_1 or condition_3)
#or requires at least one condition to be true

print(False + False)
print(False + True)
print(True + True)
print(True == 1)
print(False == 0) #in python, true and false are just words to represent 0 and 1

print(False *5)
print(True * 3 + 1) #true/false are simple stand-ins for 0 and 1

#let's continue the weirdness 
greeting = "Hello " + "world!"
print(greeting) #the plus sign operates differently when used with a string
# +, when applied to strings, means concatenation : bringing them into a single string

laugh = "ha" *3 #repetition operator
print(laugh)

weird_laugh = "ha" * 3.14 #this won't work because repetition is only with whole numbers

my_age = 25
my_intro = "I'm Abigail and I'm" + my_age #does not work because you can't concat integer to string
#returns TypeError above
#when you want types to work nicely with each other, you will need to convert them first

#Type Conversions
my_age_as_a_string = "25"
my_intro = "I'm Abigail and I'm " + my_age_as_a_string
print(my_intro)

# convert data by using the functions str, int, float, bool

#how do we use them
print(str(42))
type(str(42))

float('Hello')
float('32')
float(False)
float(40)
float('fifteen')

int('Hello')
int(True)
int('32')
int(3.14)
int(3.9) #int is cutting the decimal - it does not round numbers higher than the .5 threshold