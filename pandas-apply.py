#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.DataFrame({"product_id": [1,2,3,4,5,6,7,8,9,10],
                  "name": ["Camiseta", "Geladeira", "Televisão", "Fogão", "Sofá","Mesa","Poltrona","Computador", "Mouse", "Radio"]})


# In[3]:


df


# In[5]:


df['Categoria'] = df['name'].apply(lambda x: 'Eletrodoméstico' if x in ['Televisão', 'Computador', 'Mouse', 'Geladeira']
                                  else ('Vestuário' if x in ['Camiseta']
                                      else('Móveis'if x in ['Sofá', 'Poltrona', 'Mesa']
                                      else('Outros'))))


# In[6]:


df


# In[ ]:




