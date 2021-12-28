#!/usr/bin/env python
# coding: utf-8
	•	Write a Python program to Extract Unique values dictionary values?
	•	Write a Python program to find the sum of all items in a dictionary?
	•	Write a Python program to Merging two Dictionaries?
	•	Write a Python program to convert key-values list to flat dictionary?
	•	Write a Python program to insertion at the beginning in OrderedDict?
	•	Write a Python program to check order of character in string using OrderedDict()?
	•	Write a Python program to sort Python Dictionaries by Key or Value?

# In[5]:


##Write a Python program to Extract Unique values dictionary values?
dict1 = {'A' : [1, 3, 5, 4],
             'B' : [4, 6, 8, 10],
             'C' : [6, 12, 4 ,8],
             'D' : [5, 7, 2]}

print(dict1)
  
# Using list comprehension, values() and sorted()
res = list(sorted({ele for val in dict1.values() for ele in val}))
  
# print result 
print("The unique values list is : " , res) 


# In[11]:


##Write a Python program to find the sum of all items in a dictionary?
dic={ 'x':455, 'y':223, 'z':3200, 'p':908 }

print("Dictionary: ", dic)

#using sum() and values()
print("sum: ",sum(dic.values()))


# In[21]:


##Write a Python program to Merging two Dictionaries?
def Merge(dict1, dic):
    return(dic.update(dict1))
dict1 = {'A' : [1, 3, 5, 4],
             'B' : [4, 6, 8, 10],
             'C' : [6, 12, 4 ,8],
             'D' : [5, 7, 2]}
dic={ 'x':[12,34,455], 'y':223, 'z':3200, 'p':908 }
print(Merge(dict1, dic))
print(dic)


# In[22]:


## Write a Python program to convert key-values list to flat dictionary?
# Printing original dictionary 
languages = {'language' : ['python', 'java', 'c/c++', 'javascript'], 'year' : [1991, 1995, 1980, 1995]}

print("dictionary languages : " + str(languages))

# Flattening dictionary 
lang_year = dict(zip(languages['language'], languages['year']))

# Printing Flattened dictionary 
print("Flattened dictionary  language : " + str(lang_year))


# In[23]:


## Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict
dic1 = OrderedDict([('A', '100'), ('B', '200'), ('C', '300')])
insrt = OrderedDict([("D", '400')])
  
final = OrderedDict(list(insrt.items()) + list(dic1.items()))
  
# print result
print ("Resultant Dictionary :")
print(final)


# In[25]:


## Write a Python program to check order of character in string using OrderedDict()?
#from collections import OrderedDict 
def checkOrder(string, pattern): 
    dic = OrderedDict.fromkeys(string) 
    ptr = 0
    for key,value in dic.items(): 
        if (key == pattern[ptr]): 
            ptr = ptr + 1
        if (ptr == (len(pattern))): 
            return 'True'
    return 'False'

string = 'Study tonight'
pattern = 'stu'
print (checkOrder(string,pattern))

string2= 'Welcome'
pattern2= 'cm'
print (checkOrder(string2,pattern2)) 


# In[26]:


## Write a Python program to sort Python Dictionaries by Key or Value?
a = {1:2 ,2:1 ,4:3 ,3:4 ,6:5 ,5:6 }
#this will print a sorted list of the keys
print(sorted(a.keys()))
#this will print the sorted list with items.
print(sorted(a.items()))


# In[ ]:




