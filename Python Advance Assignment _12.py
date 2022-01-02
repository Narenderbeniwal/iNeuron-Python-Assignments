#!/usr/bin/env python
# coding: utf-8
Q1. Does assigning a value to a string indexed character violate Python string immutability?

Q2. Does using the += operator to concatenate strings violate Python& string immutability? Why or
why not?

Q3. In Python, how many different ways are there to index a character?

Q4. What is the relationship between indexing and slicing?

Q5. What is an indexed character& exact data type? What is the data form of a slicing-generated
substring?

Q6. What is the relationship between string and character in Python?

Q7. Identify at least two operators and one method that allow you to combine one or more smaller
strings to create a larger string.

Q8. What is the benefit of first checking the target string with in or not in before using the index
method to find a substring?

Q9. Which operators and built-in string methods produce simple Boolean (true/false) results?
# ##  Q1. Does assigning a value to a string indexed character violate Python string immutability?
# 
# Sol: 
#     One final thing that makes strings different from some other Python collection types is that you are not allowed to modify the individual characters in the collection. It is tempting to use the [] operator on the left side of an assignment, with the intention of changing a character in a string.

# ## Q3. In Python, how many different ways are there to index a character?
# 
# Sol:
#     
#     Each of a string's characters corresponds to an index number and each character can be accessed using their index number. We can access characters in a String in Two ways : Accessing Characters by Positive Index Number. Accessing Characters by Negative Index Number.

# ## Q4. What is the relationship between indexing and slicing?
# 
# Sol: 
#     Indexing: Indexing is used to obtain individual elements. Slicing: Slicing is used to obtain a sequence of elements. Indexing and Slicing can be be done in Python Sequences types like list, string, tuple, range objects.

# In[1]:


## Q5. What is an indexed character& exact data type? What is the data form of a slicing-generated substring?


# ## Q6. What is the relationship between string and character in Python?
# 
# Sol:
#     Python string comparison is performed using the characters in both strings. ... Both the strings are exactly the same, hence they are equal. So equality operator is returning True in this case.
# 

# ## Q7. Identify at least two operators and one method that allow you to combine one or more smaller strings to create a larger string.
# 
# Sol:
# 
# Concatenation is the process of appending one string to the end of another string. You concatenate strings by using the + operator.

# ## Q8. What is the benefit of first checking the target string with in or not in before using the index method to find a substring?
# 
# Sol ;The idea is to run a loop from start to end and for every index in the given string check whether the sub-string can be formed from that index. This can be done by running a nested loop traversing the given string and in that loop run another loop checking for sub-string from every index

# ## Q9. Which operators and built-in string methods produce simple Boolean (true/false) results?
# 
# Sol:
# 
# Logical operators are typically used with Boolean (logical) values. When they are, they return a Boolean value. However, the && and || operators actually return the value of one of the specified operands, so if these operators are used with non-Boolean values, they will return a non-Boolean value.

# In[ ]:




