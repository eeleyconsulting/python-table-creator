#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tabulate


# In[4]:


from tabulate import tabulate


# In[11]:


data = [["Name", "Place", "Gender"], ["Andile", "Cape Town", "Male"], ["Mandisa", "Johannesburg", "Female"], ["Tommy", "Kimberley", "Male"]]


# In[12]:


print(tabulate(data))


# In[13]:


print(tabulate(data, headers='firstrow'))


# In[14]:


print(tabulate(data, headers='firstrow', tablefmt='grid'))


# In[15]:


print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))


# In[ ]:




