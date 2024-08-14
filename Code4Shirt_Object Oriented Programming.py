#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Shirt:
    def __init__(self, shirt_color, shirt_style, shirt_size, shirt_price):
        self.color = shirt_color
        self.style = shirt_style
        self.size = shirt_size
        self.price = shirt_price
        
        
    def change_price(self, new_price):
        self.price = new_price
    
    def discount(self, discount):
        return self.price * (1 - discount)


# In[3]:


# instatiating the shirt object


# In[4]:


Shirt('red', 'short_sleeve', 'S', 15)


# In[5]:


# the mixed number at the end denote the location the object is stored in the memory.


# In[6]:


new_shirt = Shirt('red', 'short_sleeve', 'S', 15)


# In[7]:


print(new_shirt.color)
print(new_shirt.style)
print(new_shirt.size)
print(new_shirt.price)


# In[8]:


new_shirt.change_price(10)
print(new_shirt.price)


# In[9]:


print(new_shirt.discount(.2))


# In[10]:


tshirt_collection = []
shirt_1 = Shirt('orange', 'short_sleeve', 'S', 25)
shirt_2 = Shirt('tan', 'long_sleeve', 'XL', 35)
shirt_3 = Shirt('yellow', 'short_sleeve', 'M', 20)

tshirt_collection.append(shirt_1)
tshirt_collection.append(shirt_2)
tshirt_collection.append(shirt_3)

for i in range(len(tshirt_collection)):
    print(tshirt_collection[i].color)


# In[11]:


### TODO:
#
#    - calculate the total cost of shirt_one and shirt_two
#    - store the results in a variable called total
#    
###
total = shirt_1.price + shirt_2.price
print(total)


# In[12]:


### TODO:
#
#    - use the shirt discount method to calculate the total cost if
#       shirt_one has a discount of 14% and shirt_two has a discount
#       of 6%
#    - store the results in a variable called total_discount
###
total_discount =  shirt_1.discount(.14) + shirt_2.discount(.06)
print(total_discount)

