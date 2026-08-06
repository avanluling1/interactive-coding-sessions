import pandas as pd

# let's write a dictionary
data = {
    "Month": ['January', 'February', 'March', 'April'],
    "Marketing_Spend" : [5000, 7000, 6000, 8000],
    "Sales_Spend": [2000, 3000, 2500, 4000],
    "Leads_Generated": [150, 200, 180, 250]
}

# this dictionary is not a data frame, but it's a very good mental model
# for thinking about dataframes:
# the columns are like keys in a dictionary
# the values are arrays/lists that all have the same number of elements
# they correspond to the rows

# create a data frame from a dicionary
df = pd.DataFrame(data)
print(df)

# as you might guess, it is uncommong to type values one by one
# what is more common is reading the content of a file
df = pd.read_csv("sales_data.csv")
print(df)
print(df.head())
print(df.tail())

# second inspection
print(df.info()) # this is a method and requires parentheses

# if you need to access each of these info individually, you can:

print(df.columns) # property, not a method, so doesn't need to be called with parentheses
print(df.index)
print(df.shape) #rows and columns
print(df.dtypes) # prints datatype for each column

# actually working with dataframes.
# you can read the content of columns in your data by indexing
df["Month"] # individual columns in dataframes are called Series
print(type(df["Month"])) # series are like arrays with an index in front

# you can also ask for multiple columns:
df[["Month", "Sales_Spend"]] # indexing, and then providing a list of column names:
# that outputs a data frame!! <3

# again, repeating some content: 
# you can read with indexing...
# and you can assign values with indexing!

# Exercise 1: Increase the sales spend by 100 and save it into the dataframe
df["Sales_Spend"] = df["Sales_Spend"] + 100 # need to define df ahead of the column name

# we can also make new columns using indexing:
df["Marketing_Spend"]/df['Leads_Generated']

df["Cost_Per_Lead"] = df["Marketing_Spend"]/df['Leads_Generated']
print(df.head())

# another common operation is to filter the dataframe.
# let's say we want to see which months were particularly effective
# in acquiring leads. we want to see on which months the costs of 
# acquiring leads were less than 15.

# let's make a mask: something that, for each row, contains true or false depending on whether
# cost per lead was < 15

mask = df["Cost_Per_Lead"] < 15
df[mask]
df[ df["Cost_Per_Lead"] < 15]

# this returns a bunch of rows, whereas earlier we were indexing for columns
# there's a better way to do it: 

# the syntax is df.loc[row_index, col_index]
# use df.loc to avoid confusion

# let's say I want to see all the rows and just the columns Marketing_Spend and Sales_Spend
df.loc[:,["Marketing_Spend", "Sales_Spend"]]

df.loc[[0,2,4],["Marketing_Spend", "Sales_Spend"]]
# with the same columns

df.loc[:,"Sales_Spend"]

# use .loc to index a dataframe
# the first indexer is rows, the second is column
# remember that we are using the NAMES of rows and columns to index or mask them

# Skill 2: Summarizing Data
# both dataframes and series have methods. You can use them to get the mean(), the min(), the max(). . . 

df.loc[:,"Cost_Per_Lead"] # this will output a series
df.loc[:,"Cost_Per_Lead"].mean() # this returns one value, a scalar

# what about calling methods on a dataframe

df.loc[:, ["Sales_Spend", "Marketing_Spend"]]
df.loc[:, ["Sales_Spend", "Marketing_Spend"]].mean()
# when you call a method to summarize a data frame with numeric columns
# you are getting one value per column
# Here, we get the average marketing spend
# and the average sales spend, taken across all the rows

# now consider this second example:
df.loc[:, ["Sales_Spend", "Marketing_Spend"]].sum()

df.loc[:, ["Sales_Spend", "Marketing_Spend"]].sum(axis=1)
# sum across columns and keep rows, axis = 1
# sum across rows and keep columns, axis = 0
df.loc[:,"Total_Spend"] = df.loc[:, ["Sales_Spend", "Marketing_Spend"]].sum(axis=1)
# adding the column to the dataframe

print(df.head())

# great job! we've done some basic data cleaning and manipulation with pandas
# last step is to save our dataframe back into a file

df.to_csv("sales_data_cleaned.csv", index = False)
# index equals false says thanks, I don't need the index