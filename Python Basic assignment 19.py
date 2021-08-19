#!/usr/bin/env python
# coding: utf-8
1. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?
2. Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.
3. Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?
4. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen,' 'H,' and 1.
5. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.
6. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.
7. Call print(hydrogen). In the definition of Element, change the name of method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.
8. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.
9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.
10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.

Q. 1. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?
# In[9]:


class Thing():
    print()


# In[10]:


class Thing():
    'example'
    print()


# In[ ]:


## Printed Values are same 

Q. 2. Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.

# In[36]:


class Thing2:
    latters = 'abc'
print(Thing2.latters)


# In[34]:


class Thing2():
    
         def __init__(self,input_name):
            
              self.input_name =  input_name
            
               


# In[ ]:





# In[40]:


name = Thing2('abc')


# In[41]:


name.input_name

3. Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?
# In[45]:


class Thing3():
    
         def __init__(self,xyz):
            
              self.xyz =  xyz


# In[ ]:





# In[46]:


name = Thing3('xyz')


# In[47]:


name.xyz

4. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen,' 'H,' and 1.
# In[27]:


class Element():
    def __init__(self,name, symbol, number ):
        
        self.name = name
        self.symbol = symbol
        self.number = number


# In[48]:


Hydrogen  = Element('Hydrogen','H',1)


# In[49]:


Hydrogen.name

Q. 5. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.
# In[54]:


el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}


# In[ ]:





# In[ ]:





# In[55]:


hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])


# In[56]:


hydrogen.name


# In[ ]:





# In[ ]:




Q. 6. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.
# In[65]:


class Element():
    def __init__(self,name, symbol, number ):
        
        self.name = name
        self.symbol = symbol
    
        self.number = number
    def dump(self):
        print('name=%s, symbol=%s, number=%s' %
        (self.name, self.symbol, self.number))
hydrogen = Element(**el_dict)


# In[66]:


hydrogen = Element(**el_dict)


# In[67]:


hydrogen.dump()


# In[ ]:




Q.7. Call print(hydrogen). In the definition of Element, change the name of method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.
# In[68]:


print(hydrogen)


# In[76]:


class Element():
    def __init__(self,name, symbol, number ):
        
        self.name = name
        self.symbol = symbol
    
        self.number = number
    def __str__(self):
        return ('name=%s, symbol=%s, number=%s' %
        (self.name, self.symbol, self.number))
hydrogen = Element(**el_dict)


# In[77]:


print(hydrogen)


# In[63]:




Q. 8. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.
# In[84]:


class Element():
    def __init__(self,name, symbol, number ):
        
        
        self.name = name
        self.symbol = symbol
    
        self.number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number


# In[88]:


##hydrogen = Element('hydrogen', 'H', 1)

9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.
# In[102]:


class Bear():
    def eats(self):
        return 'berries'
class Rabbit():
    
    def eats(self):
        return 'clover'
class Octothorpe():
    
    def eats(self):
        return 'campers'


# In[103]:


b = Bear()


# In[104]:


r = Rabbit()


# In[105]:


o = Octothorpe()


# In[106]:


print(b.eats())


# In[107]:


print(r.eats())


# In[108]:


print(o.eats())

Q.10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.
# In[109]:


class Laser():
    def does(self):
        return 'disintegrate'
class Claw():
    def does(self):
        return 'crush'  
class SmartPhone():
    def does(self):
        return 'ring'  
class Robot:
    def __init__(self):
    self.laser = Laser()
    self.claw = Claw()
    self.smartphone = SmartPhone()


# In[ ]:


class Robot:
def __init__(self):
self.laser = Laser()
self.claw = Claw()
self.smartphone = SmartPhone()

