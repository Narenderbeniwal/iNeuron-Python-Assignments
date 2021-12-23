#!/usr/bin/env python
# coding: utf-8
1. What is the result of the code, and explain?


X = 'iNeuron'
def func():
print(X)


func()


2. What is the result of the code, and explain?


X = 'iNeuron'
def func():
X = 'NI!'


func()
print(X)


3. What does this code print, and why?


X = 'iNeuron'
def func():
X = 'NI'
print(X)


func()
print(X)


4. What output does this code produce? Why?


X = 'iNeuron'
def func():
global X
X = 'NI'


func()
print(X)


5. What about this code—what’s the output, and why?


X = 'iNeuron'
def func():
X = 'NI'
def nested():
print(X)
nested()


>>> func()
>>> X


6. How about this code: what is its output in Python 3, and explain?


def func():
X = 'NI'
def nested():
nonlocal X
X = 'Spam'
nested()
print(X)


func()
# In[4]:


## 1. What is the result of the code, and explain?


X = 'iNeuron'
def func():
    print(X) ## We have used the empty function in which printed the value of X


func()


# In[5]:


## 2. What is the result of the code, and explain?


X = 'iNeuron'
def func():
    X = 'NI!'


func()
print(X)


# In[8]:


##3. What does this code print, and why?


X = 'iNeuron'
def func():
    X = 'NI'
print(X)

func()
print(X) ## 1st iNeuron is printed by the use of the function and 2nd with print 


# In[10]:


## 4. What output does this code produce? Why?


X = 'iNeuron'
def func():
    global X ## used global variable and make changes to the variable in a local context.
X = 'NI'


func()
print(X)


# In[11]:


## 5. What about this code—what’s the output, and why?


X = 'iNeuron'
def func():
    X = 'NI'
def nested():
    print(X)
nested()


func()
X


# In[13]:


get_ipython().set_next_input('6. How about this code: what is its output in Python 3, and explain');get_ipython().run_line_magic('pinfo', 'explain')


def func():
    X = 'NI'
def nested():
    nonlocal X
X = 'Spam'
nested()
print(X)


func()


# In[ ]:




