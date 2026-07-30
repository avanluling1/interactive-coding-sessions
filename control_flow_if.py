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
# 