#!/usr/bin/env python
# coding: utf-8

# Q1. What is the difference between __getattr__ and __getattribute__?
# 
# 
# 
# Q2. What is the difference between properties and descriptors?
# 
# 
# 
# Q3. What are the key differences in functionality between __getattr__ and __getattribute__, as well as properties and descriptors?
# 

# ## Q1. What is the difference between __getattr__ and __getattribute__?
# Sol: 
# Getattribute: Is used to retrieve an attribute from an instance. 
# 
# Getattr: Is executed as the last resource when attribute is not found in an object
# 
# These two methods are implemented as methods of a class. __getattribute__ is always called. Essentially this method is used to find an attribute of a class. If it fails, it will raise an AttributeError. In case it fails, and class implements __getattr__, then __getattr__ is called right after. Therefore, the biggest difference is that __getattr__ is called for attributes that don’t actually exist on a class.

# ## Q2. What is the difference between properties and descriptors?
# Sol: 
#     Descriptors are a low-level mechanism that lets you hook into an object's attributes being accessed. 
#     
#     Properties are a high-level application of this; that is, properties are implemented using descriptors.

# 
# ## Q3. What are the key differences in functionality between __getattr__ and __getattribute__, as well as properties and descriptors?
# 
# ### '''__getattr__
# 
# Python will call __getattr__ method whenever you request an attribute that hasn't already been defined. In the following example my class Count has no __getattr__ method. Now in main when I try to access both obj1.mymin and obj1.mymax attributes everything works fine. But when I try to access obj1.mycurrent attribute -- Python gives me AttributeError: 'Count' object has no attribute 'mycurrent'
# '''
# 
# class Count():
# 
#     def __init__(self,mymin,mymax): 
#     
#         self.mymin=mymin 
#         
#         self.mymax=mymax
# 
# obj1 = Count(1,10)
# 
# print(obj1.mymin)
# 
# print(obj1.mymax)
# 
# #print(obj1.mycurrent) ## --> AttributeError: 'Count' object has no attribute 'mycurrent'
# 
# #Now my class Count has __getattr__ method. Now when I try to access obj1.mycurrent attribute -- python returns me whatever I have implemented in my __getattr__ method. In my example whenever I try to call an attribute which doesn't exist, python creates that attribute and sets it to integer value 0.
# 
# class Count:
#     def __init__(self,mymin,mymax): 
#     
#         self.mymin=mymin
#         
#         self.mymax=mymax    
# 
#     def __getattr__(self, item):
#     
#         self.__dict__[item]=0
#         
#         return 0
# 
# obj1 = Count(1,10)
# 
# 
# print(obj1.mymin)
# 
# print(obj1.mymax)
# 
# print(obj1.mycurrent1)
# 
# ### __getattribute__
# #Now lets see the __getattribute__ method. If you have __getattribute__ method in your class, python invokes this method for every attribute regardless whether it exists or not. So why do we need __getattribute__ method? One good reason is that you can prevent access to attributes and make them more secure as shown in the following example.
# 
# #Whenever someone try to access my attributes that starts with substring 'cur' python raises AttributeError exception. Otherwise it returns that attribute.
# 
# 
# class Count:
# 
#     def __init__(self,mymin,mymax):
#         self.mymin=mymin
#         self.mymax=mymax
#         self.current=None
#    
#     def __getattribute__(self, item):
#         if item.startswith('cur'):
#             raise AttributeError
#         return object.__getattribute__(self,item) 
#         # or you can use ---return super().__getattribute__(item)
# 
# obj1 = Count(1,10)
# print(obj1.mymin)
# print(obj1.mymax)
# #print(obj1.current)

# 
