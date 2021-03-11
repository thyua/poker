#!/usr/bin/env python
# coding: utf-8

# In[6]:


import itertools
import pprint
numbers=('A','2','3','4','5','6','7','8','9','10','J','Q','K')
symbols=('S','D','C','H')
card=itertools.product(symbols,numbers)

for v in card:
    print(v)


# In[ ]:




