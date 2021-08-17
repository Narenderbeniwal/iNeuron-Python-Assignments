#!/usr/bin/env python
# coding: utf-8
1. Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.
2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
3. Using the interpreter, explicitly import and call the hours() function from zoo.
4. Import the hours() function as info and call it.
5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.
6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?
7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].


# In[1]:


pwd(/Users/ekcs011/zoo.py)


# In[2]:


pwd()


# In[ ]:




Q. 1. Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.
# In[13]:


import zoo


# In[20]:


zoo.hours()


# In[ ]:




Q. 2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
# In[21]:


import zoo as menagerie


# In[22]:


menagerie.hours()

Q. 3. Using the interpreter, explicitly import and call the hours() function from zoo.

# In[23]:


import zoo


# In[24]:


zoo.hours()

Q. 4. Import the hours() function as info and call it.

# In[28]:


from zoo import hours as info


# In[30]:


info()

Q. 5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.

# In[31]:


dist = {'a': 1, 'b': 2, 'c': 3}


# In[32]:


dist

Q. 6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?
Ans: Yes
# In[33]:


fancy =  {'a': 1, 'b': 2, 'c': 3}


# In[34]:


fancy

Q. 7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].
# In[36]:


dict_of_lists = {list:'a'}


# In[39]:


dict_of_lists.update


# In[40]:


dict_of_lists


# In[ ]:




