#!/usr/bin/env python
# coding: utf-8
"""Question 1
Create a function that takes a number as an argument and returns True or False depending
on whether the number is symmetrical or not. A number is symmetrical when it is the same as
its reverse.
Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
is_symmetrical(1112111) ➞ True"""

# In[1]:


#Sol 1:
def is_symmetrical(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False

is_symmetrical(5115)

"""Question 2
Given a string of numbers separated by a comma and space, return the product of the
numbers.
Examples
multiply_nums("2, 3") ➞ 6
multiply_nums("1, 2, 3, 4") ➞ 24
multiply_nums("54, 75, 453, 0") ➞ 0
multiply_nums("10, -2") ➞ -20"""

# In[4]:


def multiply_nums(st):
    l=[]
    m=st.split(',')
    for i in m:
        d=int(i)
        l.append(d)
    count=0
    p=1
    while count<len(l):
        p*=l[count]
        count+=1
    return p
multiply_nums("1,2,3,4,8")
    
    

"""Question 3
Create a function that squares every digit of a number.
Examples
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer."""
# In[6]:


def square_digits(n):
    m=str(n)
    j=','.join(m)
    s=j.split(',')
    l=[]
    for i in s:
        d=int(i)
        l.append(d)
    lc=[i**2 for i in l]
    st=''.join([str(i) for i in lc])
    return int(st)


square_digits(21235565)

    

"""Question 4
Create a function that sorts a list and removes all duplicate items from it.
Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
setify([4, 4, 4, 4]) ➞ [4]
setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]"""
# In[8]:


def setify(l):
    s=set(l)
    l2=list(s)
    l2.sort()
    return l2

setify([1, 3, 3, 5, 5,2.8,2.8,1.55,1.55,1.89])

"""Question 5
Create a function that returns the mean of all digits.
Examples
mean(42) ➞ 3
mean(12345) ➞ 3
mean(666) ➞ 6
Notes
 The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in
512 is (5+1+2)/3(number of digits) = 8/3=2).
 The mean will always be an integer."""
# In[15]:


#Solution 5:
def mean(n):
    s=','.join(str(n))
    p=s.split(',')
    l=[]
    for i in p:
        d=int(i)
        l.append(d)
    return round((sum(l)/len(l)))

mean(90)


# In[ ]:




