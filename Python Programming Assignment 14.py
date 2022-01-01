#!/usr/bin/env python
# coding: utf-8
Question 1:
Define a class with a generator which can iterate the numbers, which are divisible by
7, between a given range 0 and n.

Question 2:
Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Question 3:

Define a class Person and its two child classes: Male and Female. All classes have a
method &quot;getGender&quot; which can print &quot;Male&quot; for Male class and &quot;Female&quot; for Female
class.

Question 4:
Please write a program to generate all sentences where subject is in [&quot;I&quot;, &quot;You&quot;] and
verb is in [&quot;Play&quot;, &quot;Love&quot;] and the object is in [&quot;Hockey&quot;,&quot;Football&quot;].

Question 5:
Please write a program to compress and decompress the string &quot;hello world!hello
world!hello world!hello world!&quot;.

Question 6:
Please write a binary search function which searches an item in a sorted list. The
function should return the index of element to be searched in the list.'''Question 1:
Define a class with a generator which can iterate the numbers, which are divisible by
7, between a given range 0 and n.'''
# In[3]:


n = int(input())

divby7 = [i for i in range(0,n) if (i%7==0)]
print(divby7)

def divChecker(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)

divChecker(n)


# '''
# Question 2:
# Write a program to compute the frequency of the words from the input. The output
# should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or
# Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
# '''

# In[7]:


ss = input().split()
word = sorted(set(ss))     # split words are stored and sorted as a set

for i in word:
    print("{0}:{1}".format(i,ss.count(i)))


# In[8]:


ss = input().split()
dict = {i:ss.count(i) for i in ss}     # sets dictionary as i-> split word & ss.count(i) -> total occurrence of i in ss
dict = sorted(dict.items())            # items() function returns both key & value of dictionary as a list
                                       # and then sorted. The sort by default occurs in order of 1st -> 2nd key
for i in dict:
    print("%s:%d"%(i[0],i[1]))

'''Question 3:

Define a class Person and its two child classes: Male and Female. All classes have a
method &quot;getGender&quot; which can print &quot;Male&quot; for Male class and &quot;Female&quot; for Female
class.
'''
# In[12]:


class person(object):
    def getGender( self ):
        return "Unknown"
class Male(object):
    def getGender( self ):
        return "Male"
class Female(object):
    def getGender( self ):
        return "Female"
aMale = Male()
aFemale= Female()
print(aMale.getGender())
print(aFemale.getGender())

'''Question 4:
Please write a program to generate all sentences where subject is in [&quot;I&quot;, &quot;You&quot;] and
verb is in [&quot;Play&quot;, &quot;Love&quot;] and the object is in [&quot;Hockey&quot;,&quot;Football&quot;].'''# subject=["quot","I","quot","quot","You","quot"]
verb=["quot","Play","quot","quot","Love","quot"]
obj=[["quot","Hockey","quot","quot","Football","quot"]
      
# Use list comprehension instead of looping over each of the predicates
sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
 print(sentence)

# In[20]:


'''Question 5:
Please write a program to compress and decompress the string &quot;hello world!hello
world!hello world!hello world!&quot;.'''


# In[28]:


import zlib
import binascii

data = 'Hello world'

compress = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
#compressed_data = compress.compress(data)
#compressed_data += compress.flush()

print('Original: ' + data)
#print('Compressed data: ' + binascii.hexlify(compressed_data))

'''Question 6:
Please write a binary search function which searches an item in a sorted list. The
function should return the index of element to be searched in the list.'''
# In[29]:


def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = round((low + high) / 2)
        
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
lst = [1,3,5,7,]
print(binary_search(lst, 9))   


# In[ ]:




