#!/usr/bin/env python
# coding: utf-8
"""Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated
sequence."""
# In[3]:


import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)

"""Question 2:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1."""
# In[12]:


from __future__ import print_function

user_input = input("Enter values for row and column number: ")
rows, cols = user_input.split(",")
rows = int(rows)
cols = int(cols)

grid = []
for x in range(rows):
    row = []
    for y in range(cols):
        row.append(x * y)
    grid.append(row)
    print(row)

print()
print(grid)

"""Write a program that accepts a comma separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically.
"""
# In[15]:


items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
# In[17]:


items = input("Input whitespace separated words ::")
words = [word for word in items.split(" ")]
print(" ".join(sorted(list(set(words)))))

Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.
# In[22]:


s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

Question6:

A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
# In[27]:


import re

passwords = input("Type in: ")
passwords = passwords.split(",")

accepted_pass = []
for i in passwords:
    
    if len(i) < 6 or len(i) > 12:
        continue

    elif not re.search("([a-z])+", i):
        continue

    elif not re.search("([A-Z])+", i):
        continue

    elif not re.search("([0-9])+", i):
        continue

    elif not re.search("([!@$%^&])+", i):
        continue

    else:
        accepted_pass.append(i)

print((" ").join(accepted_pass))


# In[ ]:




