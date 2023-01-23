#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


def porcentaje_nulos(a):
    return (a.isnull().sum() / a.shape[0] * 100).reset_index()


# In[5]:


def borrar_duplicados(a):
    return (a).drop_duplicates()
    

