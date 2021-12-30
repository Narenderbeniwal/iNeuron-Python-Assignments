#!/usr/bin/env python
# coding: utf-8

# """Question1
# Write a function that takes a list and a number as arguments. Add the number to the end of
# the list, then remove the first element of the list. The function should then return the updated
# list."""
# 

# In[4]:


def next_line(lst,n):
    for i in range(len(lst)):
        if i==0:
            lst.remove(lst[i])
            lst.append(n)
            return lst
next_line([1,5,8,9,20,47],17)


# """Question2
# Create the function that takes a list of dictionaries and returns the sum of people's budgets."""
# 

# In[6]:


def get_budget(dic):
    l=[]
    for i in dic:
        for j in i:
            if j=='budget':
                l.append(i[j])
    return sum(l)
get_budget([{'name':'jhon','age':22,'budget':22000},{'name':'nirmala','age':52,'budget':52000},
            {'name':'jetly','age':55,'budget':80000},{'name':'siddharth','age':35,'budget':62000}])


# """Question3
# Create a function that takes a string and returns a string with its letters in alphabetical order."""
# 

# In[18]:


def alpha_sort(st):
    return ''.join(sorted(st))
alpha_sort('narender')


# """Question4
# Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly.
# What will be the value of your investment at the end of the 10 year period?
# Create a function that accepts the principal p, the term in years t, the interest rate r, and the
# number of compounding periods per year n. The function returns the value at the end of term
# rounded to the nearest cent.
# For the example above:
# compound_interest(10000, 10, 0.06, 12) ➞ 18193.97
# Note that the interest rate is given as a decimal and n=12 because with monthly compounding
# there are 12 periods per year. Compounding can also be done annually, quarterly, weekly, or
# daily."""

# In[20]:


def compound_interest(p,t,r,n):
    CI=p*(1+r/n)**(n*t)
    return round(CI,2)
compound_interest(10000,12,0.06,12)


# In[21]:


"""Question5
Write a function that takes a list of elements and returns only the integers."""


# In[23]:


def return_only_int(lst):
    return [i for i in lst if type(i)==int]
return_only_int([2,'apl',2.65,'asdf',[2,11],35,66,99,88,33,45,6,7,8,9])


# In[ ]:




