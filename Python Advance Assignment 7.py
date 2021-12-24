#!/usr/bin/env python
# coding: utf-8




# ## Q1. What is the purpose of the try statement?
# 
# Sol: Try and Except statement is used to handle these errors within our code in Python. The try block is used to check some code for errors i.e the code inside the try block will execute when there is no error in the program. Whereas the code inside the except block will execute whenever the program encounters some error in the preceding try block.
# 
# try:
# 
#     # Some Code
#     
# except:
# 
#     # Executed if error in the
#     # try block
# 
# How try() works? 
#  
# 
# First, the try clause is executed i.e. the code between try and except clause.
# 
# If there is no exception, then only the try clause will run, except the clause is finished.
# 
# If any exception occurs, the try clause will be skipped and except clause will run.
# 
# If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops.
# 
# A try statement can have more than one except clause
# 

# ## Q2. What are the two most popular try statement variations?
# Sol: 
#     Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program.
#     
# Some of the common Exception Errors are : 
#  
# 
# IOError: if the file can’t be opened
# 
# KeyboardInterrupt: when an unrequired key is pressed by the user
# 
# ValueError: when built-in function receives a wrong argument
# 
# EOFError: if End-Of-File is hit without reading any data
# 
# ImportError: if it is unable to find the module
# 

# ## Q3. What is the purpose of the raise statement?
# 
# Sol: The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.
# 

# ## Q4. What does the assert statement do, and what other statement is it like?
# 
# Sol: Assert statement takes an expression and optional message. Assert statement is used to check types, values of argument and the output of the function. Assert statement is used as debugging tool as it halts the program at the point where an error occurs.
# 
#      

# ## Q5. What is the purpose of the withstatement in python?
# 
# Sol: With statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams.

# In[ ]:




