#!/usr/bin/env python
# coding: utf-8

# In[5]:


import itertools
import pprint
numbers=range(1,14)
symbols=('a','b','c','d')
card=itertools.product(numbers,symbols)

for v in card:
    print(v)


# In[ ]:




