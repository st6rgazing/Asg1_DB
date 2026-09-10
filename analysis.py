import pandas as pd
import numpy as np

df = pd.read_csv('Assignment 1/online_delivery.csv')

# print the first 2 rows
print("First 2 rows:")
print(df.head(2))
print ("\n")

# print the first row
print("First row:")
print(df.head(1))
print ("\n")

# print rows 10-19
print("Rows 10-19:")
print(df.iloc[10:19])
print ("\n")

#print column names
print("Column names:")
print(df.columns)
print ("\n")

#print the first 10 values of one column
print("First 10 values of one column:")
print(df['Age'].head(10))
print ("\n")

#print the first 10 rows of three columns
print("First 10 rows of three columns:")
print(df[['Age', 'Gender', 'Marital Status']].head(10))
print ("\n")



print ("--------------------------------")

print("What % of customers who ordered are married?")
#creating a new dataframe with only the married customers
married = df[df['Marital Status'] == 'Married']
#checking ratio of length of married customers df to total customers df
print(round(len(married)/len(df) * 100),"%")



print("What % of customers who ordered are students?")
students = df[df['Occupation'] == 'Student']
#checking ratio of length of students customers df to total customers df
print(round(len(students)/len(df) * 100),"%")

print("What is the average family size of customers?")
print(df['Family size'].mean().round(2))

print ("--------------------------------")