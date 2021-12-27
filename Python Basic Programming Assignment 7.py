#!/usr/bin/env python
# coding: utf-8

# 	•	Write a Python Program to find sum of array?
# 	•	Write a Python Program to find largest element in an array?
# 	•	Write a Python Program for array rotation?
# 	•	Write a Python Program to Split the array and add the first part to the end?
# 	•	Write a Python Program to check if given array is Monotonic?
# 

# In[9]:


## Write a Python Program to find sum of array? 
arr = []

arr = [2,3,4,5,6,7,8,35]

print(sum(arr))


# In[20]:


## Write a Python Program to find largest element in an array?

#Initialize array     
arr = [25, 11, 7, 75, 56,4234,423]
#Initialize max with first element of array.    
max = arr[0];    
     
#Loop through the array    
for i in range(0, len(arr)):    
    #Compare elements of array with max    
   if(arr[i] > max):    
       max = arr[i];    
           
print("Largest element present in given array: " + str(max));   


# In[21]:


## Write a Python Program for array rotation?
def rotateArray(a,d):
    temp = []
    n=len(a)
    for i in range(d,n):
        temp.append(a[i])
    i = 0
    for i in range (0,d):
        temp.append(a[i])
    a=temp.copy()
    return a
 
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, 2))


# In[23]:


## Write a Python Program to Split the array and add the first part to the end?
def SplitArray(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]

        arr[n-1] = x
arr = [15, 40, 15, 16, 50, 36]
n = len(arr)
position = 2
SplitArray(arr, n, position)
for i in range(0, n):
    print(arr[i], end = ' ')


# In[24]:


## Write a Python Program to check if given array is Monotonic?

#check if monotone
#function definition
def ismonotone(a):
    n=len(a) #size of array
    if n==1:
        return True
    else:
        #check for monotone behaviour
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False

A = [6, 5, 4, 2]
print(ismonotone(A))
b = [6, 2, 4, 2]
print(ismonotone(b))
c=[4,3,2]
print(ismonotone(c))
d=[1]
print(ismonotone(d))


# In[ ]:




