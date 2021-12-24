#!/usr/bin/env python
# coding: utf-8
1. Add the current date to the text file today.txt as a string.
2. Read the text file today.txt into the string today_string
3. Parse the date from today_string.
4. List the files in your current directory
5. Create a list of all of the files in your parent directory (minimum five files should be available).
6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.
7. Create a date object of your day of birth.
8. What day of the week was your day of birth?
9. When will you be (or when were you) 10,000 days old?
# In[12]:


## Q. 1. Add the current date to the text file today.txt as a string.
# importing datetime module
import datetime
  
# datetime.datetime.now() to get 
# current date as filename.
filename = datetime.datetime.now()
  
# create empty file
def create_file():
    # Function creates an empty file
    # %d - date, %B - month, %Y - Year
    with open(filename.strftime("%d %B %Y")+".txt", "w") as file:
        file.write("")
  
# Driver Code
create_file()


# In[ ]:


## 2. Read the text file today.txt into the string today_string


# In[14]:


## 3. Parse the date from today_string.
from datetime import datetime

date_time_str = '18/09/19 01:55:19'

date_time_obj = datetime. strptime(date_time_str, '%d/%m/%y %H:%M:%S')


print ("The type of the date is now", type(date_time_obj))


# In[16]:


## 4. List the files in your current directory
dir()


# In[18]:


## 7. Create a date object of your day of birth.
import datetime
birthday=input("What is your B'day? (in DD/MM/YYYY) ")
birthdate=datetime. datetime. strptime(birthday,"%d/%m/%Y"). date()
print("Your B'day is : "+birthdate. strftime('%d/%B/%Y'))


# In[19]:


## 8. What day of the week was your day of birth?
import datetime
from datetime import date
import calendar
 
def findDay(date):
    day, month, year = (int(i) for i in date.split(' '))   
    born = datetime.date(year, month, day)
    return born.strftime("%A")
 
# Driver program
date = '26 12 1995'
print(findDay(date))


# In[24]:


## 9. When will you be (or when were you) 10,000 days old?

from datetime import datetime
str(datetime.now() - datetime(1994, 8, 8))


# In[ ]:




