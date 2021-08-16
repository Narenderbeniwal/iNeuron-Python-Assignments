#!/usr/bin/env python
# coding: utf-8
1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.
3.In the years list, which year were you the oldest?
4. Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."
7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
9. Write the French word for walrus in your three-word dictionary e2f.
10. Make a French-to-English dictionary called f2e from e2f. Use the items method.
11. Print the English version of the French word chien using f2e.
12. Make and print a set of English words from the keys in e2f.
13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.
14. Print the top-level keys of life.
15. Print the keys for life['animals'].
16. Print the values for life['animals']['cats']


# In[5]:


##1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980.
## the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
years_list = [1995,1996,1997,1998,2000]


# In[6]:


## 2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.
years_list[2]


# In[7]:


## 3.In the years list, which year were you the oldest?
years_list[4]


# In[9]:


## 4. Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
list = ["mozzarella", "cinderella", "salmonella"]

Q. 5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
Ans. No this don't change the elsement in the list.
# In[10]:


list = ["narender",'beniwal','lion ']


# In[13]:


list[0].capitalize()


# In[14]:


list

##6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."

# In[18]:


surprise_list = ["Groucho", "Chico", "Harpo"]

Q. 7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
# In[25]:


last  = surprise_list[2].lower()[::-1]


# In[27]:


last


# In[28]:


last.capitalize()


# In[29]:


surprise_list

Q. 8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
# In[33]:


e2f = {'dog': 'chien', 'cat': 'chat','walrus': 'morse'}


# In[34]:


e2f.keys()


# In[35]:


e2f.items()


# In[36]:


e2f.values()

Q. 9. Write the French word for walrus in your three-word dictionary e2f.

# In[45]:


e2f.values()

Q. 10. Make a French-to-English dictionary called f2e from e2f. Use the items method.

# In[47]:


f2e = {'chien': 'dog', 'chat': 'cat','morse': 'walrus'}

Q. 11. Print the English version of the French word chien using f2e.

# In[48]:


f2e.values()

Q. 12. Make and print a set of English words from the keys in e2f.

# In[49]:


e2f.keys()

Q. 13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.
# In[ ]:





# In[51]:


life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': '',
        'emus': '',
        },
    'plants': '',
    'other': ''
    }


# In[52]:


life

Q. 14. Print the top-level keys of life.

# In[53]:


life.keys()

Q. 15. Print the keys for life['animals'].

# In[54]:


life['animals'].keys()

16. Print the values for life['animals']['cats']

# In[55]:


life['animals']['cats']


# In[ ]:




