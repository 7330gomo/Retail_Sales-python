# Databricks notebook source
#Importing all relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# COMMAND ----------

#load Dataset from the table using spark
df = spark.table('retail.sales.data')
retail= df.toPandas()


# COMMAND ----------

# MAGIC %md
# MAGIC Understanding the data

# COMMAND ----------

#Getting a high level summary of the tabled
retail.info()

# COMMAND ----------

#Describing the table and gives statistical info about the table
retail.describe()

# COMMAND ----------

#Listing the table columns
retail.columns

# COMMAND ----------

#Show all columns
display(retail)

# COMMAND ----------

#Gives a snapshot of data
print(retail)

# COMMAND ----------

#Shows first five rows of the table
retail.head()

# COMMAND ----------

#Shows the last five rows of the table
retail.tail()

# COMMAND ----------

#To check duplicates and how many are they
retail.duplicated().sum()

# COMMAND ----------

#Checking for null values and how many are they
retail.isnull().sum()

# COMMAND ----------

#Show the number of rows-1000 and columns-9
retail.shape

# COMMAND ----------

#Deletes rows with missing values
retail=retail.dropna()

# COMMAND ----------

#substituting the missing values with 0
retail=retail.fillna(0)


# COMMAND ----------

#Show the data types of the columns
retail.dtypes

# COMMAND ----------

#to 
display(retail)


# COMMAND ----------

#converting the date datatype from object to date / to change the data types
print(pd.DatetimeIndex(retail['Date']))

# COMMAND ----------

# To see the data types after converting the data type of the date column above
retail.dtypes

# COMMAND ----------

#Created three new colums by splitting the date columns into year,month,day
Date_column=pd.DatetimeIndex(retail['Date'])
retail['Year']=Date_column.year
retail['Month']=Date_column.month
retail['Day']=Date_column.day



# COMMAND ----------

#To see the three new columns
display(retail)

# COMMAND ----------

#Group by month and sum the total amount/ shows revenue by months
retail.groupby('Month')['Total Amount'].sum()

# COMMAND ----------

# Sales by category (Matplotlib)
sales_by_category = retail.groupby('Product Category')['Total Amount'].sum()
plt.figure() #Creating the canvas
sales_by_category.plot(kind='bar')
#plt.plot(Sales_by_category)
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()


# COMMAND ----------

# Sales Trend Over Time
retail['Date'] = pd.to_datetime(retail['Date'])
sales_trend = retail.groupby('Date')['Total Amount'].sum()
plt.figure()
sales_trend.plot()
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# COMMAND ----------

# Seaborn - Sales by Month
plt.figure()
sns.barplot(data=retail, x='Month', y='Total Amount')
plt.title('Sales by Month')
plt.show()
