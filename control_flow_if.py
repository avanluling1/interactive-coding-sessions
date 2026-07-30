# we are going to talk about control flow
# control flow is instructions that determine when, whether, and how often
# a section of the code is going to run. 

my_name = 'Abigail'
my_gender = 'Female'

if my_gender == 'Female': 
    print("Hello Ms. " + my_name)
elif my_gender == 'Male':
    print("Hello Mr." + my_name)
elif my_gender == 'Non-Binary':
    print("Hello" + my_name)
else:
    print("Hello" + my_name + ", how should I address you?")

# anatomy of an if statement:
# an if statement begins with a keyword if
# after the if statement, we have a logical statement/logical test,
# or logical expression (something that evals to true or false)
# after that, we have a colon:
# on the next line follows an indented code block: 
# the indented code block is what the machine will run IF the logical statement
# evaluates to true

# after this code block, you can have between zero and many ELIF statements.
# structure: elif LOGICAL STATEMENT: 
# each followed by their own code block:
# these code blocks will run when the associated logical statement is true AND
# none of the previous values were true

# conditional logic blocks run sequentially, one statement at a time
# and they stop at the first True statement that they encounter.
# the final statement can be (but does not have to be) an ELSE statement:
# else, note that there is no condition
# when will else run? 
# only when all the statements have evaluated to false

# VERY COMMON GOTCHA WITH CONDITIONAL STATEMENTS:

def status_checker(age):
    if age >= 18:
        print("You are an adult")
    elif age >= 13:
        print("You are a teenager")
    elif age >= 4:
        print("You are a kid")
    else:
        print("You are a baby")

status_checker(1)
status_checker(5)
status_checker(17)
status_checker(39)

# order statements from most restrictive to least restrictive

def can_legally_drink(country, age):
    if (country == "USA"):
        if (age >= 21):
            return True
        else: 
            return False
    elif (country == "Canada"):
        if (age >= 19):
            return True
        else:
            return False
    elif (country == "Germany"):
        if (age >= 16):
            return True
        else:
            return False
    else: 
        return "Don't know"

# trick 1: You can write a simple if statement in one line
# that's called the "TERNARY OPERATOR":

age = 20
status = "adult" if age >= 18 else "minor"
# value_if_true if <logical statement> else value_if_false

# trick 2: you can sometimes save yourself a lot of effort by using a dictionary 
# rather than an if statement

# let's say you want ot map countries to their currency: 

def get_country_currency(country):
    if country == "USA":
        return "US Dollars"
    elif country == "Canada":
        return "Canadian Dollars"
    elif country == "France":
        return "Euros"
    elif country == "Japan":
        return "Yen"
    else:
        return "Country not found"

# this is good but not great
# we are always checking the value of one variable (country)
# and depending on the value we are returning another

# it works a lot like a dictionary
country_currency = {
    "USA" : "US Dollars",
    "Canada" : "Canadian Dollars",
    "France" : "Euros",
    "Japan" : "Yen"
}

# how do we get the currency from here
country_currency["France"]

get_country_currency("Iran")
country_currency['Iran'] # this returns a key error

# however
country_currency.get("Iran","Country not found")

