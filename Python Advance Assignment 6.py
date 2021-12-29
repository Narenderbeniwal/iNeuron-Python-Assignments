#!/usr/bin/env python
# coding: utf-8

# Q1. Describe three applications for exception processing.
# 
# Q2. What happens if you don't do something extra to treat an exception?
# 
# Q3. What are your options for recovering from an exception in your script?
# 
# Q4. Describe two methods for triggering exceptions in your script.
# 
# Q5. Identify two methods for specifying actions to be executed at termination time, regardless of
# whether or not an exception exists.

# ## Q1. Describe three applications for exception processing.
# Sol: 
#     There are three types of exception—the checked exception, the error and the runtime exception.

# ## Q2. What happens if you don't do something extra to treat an exception?
# Sol:
#     
#     When an exception occurred, if you don't handle it, the program terminates abruptly and the code past the line that caused the exception will not get executed.

# ## Q3. What are your options for recovering from an exception in your script?
# Sol :
#     
# Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause

# ## Q4. Describe two methods for triggering exceptions in your script.
# Sol :
#     
# As a Python developer you can choose to throw an exception if a condition occurs. To throw (or raise) an exception, use the raise keyword.
# 
# In some situations, you might want to run a certain block of code if the code block inside try ran without any errors. For these cases, you can use the optional else keyword with the try statement.
# 
# 

# ## Q5. Identify two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists.
# 
# 
# Sol: 
# The optional else clause contains codes to be executed if no exception occurs. The optional finally block contains codes to be executed irrespective of whether an exception occurs or not.

# In[ ]:




