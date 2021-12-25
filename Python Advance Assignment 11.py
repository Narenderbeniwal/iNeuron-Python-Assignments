#!/usr/bin/env python
# coding: utf-8

# Q1. What is the concept of a metaclass?
# 
# 
# 
# Q2. What is the best way to declare a class's metaclass?
# 
# 
# 
# Q3. How do class decorators overlap with metaclasses for handling classes?
# 
# 
# 
# 
# 

# ## Q1. What is the concept of a metaclass?
# 
# Sol: 
#     
# A metaclass in Python is a class of a class that defines how a class behaves. A class is itself an instance of a metaclass. A class in Python defines how the instance of the class will behave.
# 
# ![meta_classes.png](attachment:meta_classes.png)

# ## Q2. What is the best way to declare a class's metaclass?
# Sol: 
#     In order to set metaclass of a class, we use the __metaclass__ attribute. Metaclasses are used at the time the class is defined, so setting it explicitly after the class definition has no effect.
# 
# 

# ## Q3. How do class decorators overlap with metaclasses for handling classes?
# Sol: 
# 
# 
# Just like with metaclasses, because the decorator returns the original class, instances are made from it, not from a wrapper object. In fact, instance creation is not intercepted at all. ... Decorators can be used to manage both instances and classes, and they intersect with metaclasses in the second of these roles.
# 

# In[ ]:




