#!/usr/bin/env python
# coding: utf-8

# 	•	Write a Python program to check if the given number is a Disarium Number?
# 	•	Write a Python program to print all disarium numbers between 1 to 100?
# 	•	Write a Python program to check if the given number is Happy Number?
# 	•	Write a Python program to print all happy numbers between 1 and 100?
# 	•	Write a Python program to determine whether the given number is a Harshad Number?
# 	•	Write a Python program to print all pronic numbers between 1 and 100?
# 

# In[14]:


## Write a Python program to check if the given number is a Disarium Number?

n = 125
if 1*1+2*2+5*5 ==125:
    print("number is a Disarium Number ")
else: 
    print("number is not a Disarium Number")


# In[15]:


## Write a Python program to print all disarium numbers between 1 to 100?
#calculateLength() will count the digits present in a number    
def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
#sumOfDigits() will calculates the sum of digits powered with their respective position    
def sumOfDigits(num):    
    rem = sum = 0;    
    len = calculateLength(num);    
        
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     
#Displays all disarium numbers between 1 and 100    
print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):    
    result = sumOfDigits(i);    
        
    if(result == i):    
        print(i),    


# In[16]:


## Write a Python program to check if the given number is Happy Number?
def isHappy(n):    
    r = s = 0;    
    while(n > 0):    
        r = n%10    
        s += r**2  
        n //= 10    
    return s  
        
n = int(input())    
res = n;    
     
while(res != 1 and res != 4):    
    res = isHappy(res)    
     
if(res == 1):    
    print("happy number");    
elif(res == 4):    
    print("not a happy number");   


# In[ ]:


## Write a Python program to print all happy numbers between 1 and 100?
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Happy numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
    num=i
    sum=0
    while sum != 1 and sum != 4:
        sum = 0
        while num != 0:
            rem = num % 10
            sum += (rem * rem)
            num //= 10
        num = sum

    if sum == 1:
        print(i,end=" ")


# In[17]:


## # Harshad Number

# Reading number
number = int(input('Enter number: '))

# Making copy of number for later use
copy = number

# Finding sum of digit
digit_sum = 0

while number:
    digit_sum += number%10
    number //= 10

# Checking divisibility & making decision
if copy%digit_sum == 0:
    print('%d is Harshad Number' % (copy))
else:
    print('%d is Not Harshad Number' % (copy))

# Harshad Number

# Reading number
number = int(input('Enter number: '))

# Making copy of number for later use
copy = number

# Finding sum of digit
digit_sum = 0

while number:
    digit_sum += number%10
    number //= 10

# Checking divisibility & making decision
if copy%digit_sum == 0:
    print('%d is Harshad Number' % (copy))
else:
    print('%d is Not Harshad Number' % (copy))


# In[18]:


## Write a Python program to print all pronic numbers between 1 and 100?
## isPronicNumber() will determine whether a given number is a pronic number or not    
def isPronicNumber(num):    
    flag = False;    
        
    for j in range(1, num+1):    
        #Checks for pronic number by multiplying consecutive numbers    
        if((j*(j+1)) == num):    
            flag = True;    
            break;    
    return flag;    
     
#Displays pronic numbers between 1 and 100    
print("Pronic numbers between 1 and 100: ");    
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        print(i),    
        print(" "),    


# In[ ]:





# In[ ]:




