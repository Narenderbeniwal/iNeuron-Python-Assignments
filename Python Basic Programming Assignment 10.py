#!/usr/bin/env python
# coding: utf-8

# 	•	Write a Python program to find sum of elements in list?
# 	•	Write a Python program to  Multiply all numbers in the list?
# 	•	Write a Python program to find smallest number in a list?
# 	•	Write a Python program to find largest number in a list?
# 	•	Write a Python program to find second largest number in a list?
# 	•	Write a Python program to find N largest elements from a list?
# 	•	Write a Python program to print even numbers in a list?
# 	•	Write a Python program to print odd numbers in a List?
# 	•	Write a Python program to Remove empty List from List?
# 	•	Write a Python program to Cloning or Copying a list?
# 	•	Write a Python program to Count occurrences of an element in a list?
# 

# In[9]:


## Write a Python program to find sum of elements in list?
# creating a list
list = [11, 5, 17, 18, 23,89]
 
# using sum() function
total = sum(list)
 
# printing total value
print("Sum of all elements in given list: ", total)


# In[10]:


# Python program to find sum of elements in list
total = 0
 
# creating a list
list1 = [11, 5, 17, 18, 23]
 
# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]
 
# printing total value
print(total)


# In[13]:


## Write a Python program to  Multiply all numbers in the list?
total = 1

list2 = [22,3,4,5,6,5,75,76,86,8]

for ele in range(0, len(list2)):
    total = total*list2[ele]
print(total)


# In[19]:


## Write a Python program to find smallest number in a list?
list3 = [12,3,4,5,6,7,8,9]
list3.sort()
smallest = min(list3)

print(smallest)


# In[21]:


## Write a Python program to find largest number in a list?
list3 = [12,3,4,5,6,7,8,9,352354]
list3.sort()
largest = max(list3)

print(largest)


# In[23]:


##Write a Python program to find second largest number in a list?
list3 = [12,3,4,5,6,7,8,9,352354]
list3.sort()
largest = max(list3)

print(largest)


# In[24]:


## Write a Python program to find second largest number in a list?
list4 = [12,3,4,5,6,7,8,9,35]
list4.sort()
print(list4[-2])


# In[25]:


## Write a Python program to find N largest elements from a list?
l = [1000,298,3579,100,200,-45,900]
n = 4
  
l.sort()
print(l[-n:])


# In[31]:


##Write a Python program to print even numbers in a list?
list1 = [12,3,3,4,5,4,5,6,7,8,8]

for num in list1:
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")


# In[32]:


## Write a Python program to print odd numbers in a List?
list1 = [12,3,3,4,5,4,5,6,7,8,8]

for num in list1:
 
    # checking condition
    if num % 2 != 0:
        print(num, end=" ")


# In[38]:


## Write a Python program to Remove empty List from List?

# Initializing list
myList = [1, [], 2, 3, [], 4, 5, [], [], 9]

# printing original list
print("The original list is : " + str(myList))

# Remove empty List from List
result = [ele for ele in myList if ele != []]

print ("List after empty list removal : " + str(result))


# In[40]:


## Write a Python program to Cloning or Copying a list?
my_list = [1, 2, 3, 4, 5]
copy_list = my_list
print('Old List: ', my_list)
print('New List: ', copy_list)


# In[45]:


## Write a Python program to Count occurrences of an element in a list?
list1 = [12,3,3,4,5,4,5,6,7,8,8]
list1.count(3)


# In[ ]:




