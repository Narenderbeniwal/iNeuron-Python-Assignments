#!/usr/bin/env python
# coding: utf-8

# Q1. What is the meaning of multiple inheritance?
# 
# Q2. What is the concept of delegation?
# 
# Q3. What is the concept of composition?
# 
# Q4. What are bound methods and how do we use them?
# 
# Q5. What is the purpose of pseudoprivate attributes?

# ## Q. 1 What is the meaning of multiple inheritance?
# 
# Sol: When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.

# ## Q2. What is the concept of delegation?
# Sol:
#     
#     Delegation means that you use an object of another class as an instance variable, and forward messages to the instance.
#     Let's say you have an object x and want to change the behaviour of just one of its methods. You can create a new class that provides a new implementation of the method you're interested in changing and delegates all other methods to the corresponding method of x. Python programmers can easily implement delegation.
# 
#     

# ## Q3. What is the concept of composition?
# Sol: 
#     In composition, one of the classes is composed of one or more instance of other classes.
#     
#     Composition is a concept that models a has a relationship. It enables creating complex types by combining objects of other types. This means that a class Composite can contain an object of another class Component . This relationship means that a Composite has a Component .
# 

# ## Q4. What are bound methods and how do we use them?
# 
# Sol: 
# 
#     A bound method is the one which is dependent on the instance of the class as the first argument. It passes the instance as the first argument which is used to access the variables and functions. In Python 3 and newer versions of python, all functions in the class are by default bound methods.
# 

# ## Q5. What is the purpose of pseudoprivate attributes?
# 
# Sol:
#     
#     This is sometimes misleadingly called private attributes really, it's just a way to localize a name to the class that created it, and does not prevent access by code outside the class. That is, this feature is mostly intended to avoid namespace collisions in instances, not to restrict access to names in general.

# In[ ]:




