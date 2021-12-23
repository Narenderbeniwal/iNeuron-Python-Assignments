#!/usr/bin/env python
# coding: utf-8
1. What is the result of the code, and why?
>>> def func(a, b=6, c=8):
print(a, b, c)
>>> func(1, 2)
2. What is the result of this code, and why?
>>> def func(a, b, c=5):
print(a, b, c)
>>> func(1, c=3, b=2)
3. How about this code: what is its result, and why?
>>> def func(a, *pargs):
print(a, pargs)
>>> func(1, 2, 3)
4. What does this code print, and why?
>>> def func(a, **kargs):
print(a, kargs)
>>> func(a=1, c=3, b=2)
5. What gets printed by this, and explain?
>>> def func(a, b, c=8, d=5): print(a, b, c, d)
>>> func(1, *(5, 6))
6. what is the result of this, and explain?
>>> def func(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y'
>>> l=1; m=[1]; n={'a':0}
>>> func(l, m, n)
>>> l, m, n


# In[17]:


## 1. What is the result of the code, and why?
def func(a, b=6, c=8):
    print(a, b, c)
func(1, 2)## Here we are giving the value of a=1 And b = 2, function will take the value of the c as it is we have given c=8


# In[18]:


## 2. What is the result of this code, and why?
def func(a, b, c=5):
    print(a, b, c)
func(1, c=3, b=2)
## Here we are giving the value of a=1 And b = 2,and value of c=3 and it will print the same print(a, b, c)


# In[4]:


## 3. How about this code: what is its result, and why?
def func(a, *pargs):
    print(a, pargs)
func(1, 2, 3)


# In[19]:


## 4. What does this code print, and why?
def func(a, **kargs):
    print(a, kargs)
func(a=1, c=3, b=2) 
## **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
## It will print a as it is and conver the b and c in key value as we have used the **kargs


# In[11]:


### 5. What gets printed by this, and explain?
def func(a, b, c=8, d=5): 
    print(a, b, c, d)
func(1, *(5, 6))


# In[16]:


## 6. what is the result of this, and explain?
def func(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y'
l=1; m=[1]; 
n={'a':0}
func(l, m, n)
l, m, n


# In[ ]:




