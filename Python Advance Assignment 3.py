#!/usr/bin/env python
# coding: utf-8

# 1. What is the concept of an abstract superclass?
# 
# 
# 
# 2. What happens when a class statement's top level contains a basic assignment statement?
# 
# 
# 
# 3. Why does a class need to manually call a superclass's __init__ method?
# 
# 
# 
# 4. How can you augment, instead of completely replacing, an inherited method?
# 
# 
# 
# 5. How is the local scope of a class different from that of a function?
# 

# ## Q. 1. What is the concept of an abstract superclass?
# 
# Sol: An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class.
# 
# 

# ## Q. 2. What happens when a class statement's top level contains a basic assignment statement?
# 
# Sol: 
# An assignment statement evaluates the expression list (remember that this can be a single expression or a comma-separated list, the latter yielding a tuple) and assigns the single resulting object to each of the target lists, from left to right.

# ## Q. 3. Why does a class need to manually call a superclass's __init__ method?
# Sol: 
#     It's because one needs to define something that is NOT done in the base-class' __init__ , and the only possibility to obtain that is to put its execution in a derived-class' __init__ function.

# In[1]:


## Q. 4 How can you augment, instead of completely replacing, an inherited method?


# ## Q. 5. How is the local scope of a class different from that of a function?
# 
# Sol: 
#     Since local variables are only recognized inside their functions, variables with the same name can be used in different functions. Local variables are created when a function starts, and deleted when the function is completed.
# 

# In[ ]:




