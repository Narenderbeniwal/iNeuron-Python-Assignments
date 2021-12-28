#!/usr/bin/env python
# coding: utf-8
	•	Write a Python program to find words which are greater than given length k?
	•	Write a Python program for removing i-th character from a string?
	•	Write a Python program to split and join a string?
	•	Write a Python to check if a given string is binary string or not?
	•	Write a Python program to find uncommon words from two Strings?
	•	Write a Python to find all duplicate characters in string?
	•	Write a Python Program to check if a string contains any special character?

# In[10]:


## Write a Python program to find words which are greater than given length k?
def word_k(k, s):    
    # split the string where space comes
    word = s.split(" ")
    # iterate the loop for every word
    for x in word:
        # if length of current word
        if len(x)>k:
          # greater than k then
          print(x)
k = 5
s ="Python is good"
word_k(k, s)


# In[13]:


## Write a Python program for removing i-th character from a string?
# Python code to demonstrate method 
# to remove i-th character

myStr =  input('Enter the string : ')
i = int(input('Enter the index of character to be removed : '))

resStr = ""

for index in range(len(myStr)):
    if index != i:
        resStr = resStr + myStr[index]

# Printing all strings... 
print ("Entered string : " + myStr)
print ("String formed by removing i'th character : " + resStr)


# In[21]:


## Write a Python program to split and join a string?
s = "my name is narender beniwal"
s.split()


# In[27]:


#string joining
str1=input("Enter first String   :: ")
str2=input("Enter second String  :: ")
str=str2.join(str1)     #each character of str1 is concatenated to the #front of str2
print(str)


# In[34]:


## Write a Python to check if a given string is binary string or not?
def check(string) :
    b = set(string)
    s = {'0', '1'}
    if s == b or b == {'0'} or b == {'1'}:
        print("Binary String")
    else :
        print("Non Binary String")
  
s1= "00110101"
# function calling
check(s1)
s2 = "1010100200111"
check(s2)


# In[35]:


## Write a Python program to find uncommon words from two Strings?
# Python program to find uncommon words from two string,

# Getting strings as input from the user 
str1 = input('Enter first string : ')
str2 = input('Enter second string : ')

# finding uncommon words
count = {}
for word in str1.split():
    count[word] = count.get(word, 0) + 1
for word in str2.split():
    count[word] = count.get(word, 0) + 1
  
uncommonWords =  [word for word in count if count[word] == 1]

# printing uncommon words 
print("All uncommon words from both the string are ", uncommonWords)


# In[37]:


## Write a Python to find all duplicate characters in string?
string = input("enter the string whose duplicate characters you want to find:")

def duplicates_char(s):
    elements = {}
    for char in s:
        if elements.get(char,None) != None:
            elements[char]+=1
        else:
            elements[char] = 1
    return [k for k,v in elements.items() if v>1]
print("the duplicate character in",string,"is")
print(duplicates_char(string))


# In[42]:


## Write a Python Program to check if a string contains any special character?
special_characters = "!@#$%^&*()-+?_=,<>/"
s=input()


if any(c in special_characters for c in s):
    print("yes")
else:
    print("no")


# In[ ]:




