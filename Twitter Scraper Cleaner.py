#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 


# In[ ]:


data = pd.read_csv('Insert your CSV')


# In[ ]:


data


# In[ ]:


data['content'] = data['content'].str.replace(r'\W', " ")


# In[ ]:


data


# In[ ]:


data.likes = (data.likes.replace(r'[KM]+$', '', regex=True).astype(float) *           data.likes.str.extract(r'[\d\.]+([KM]+)', expand=False)
            .fillna(1)
            .replace(['K','M'], [10**3, 10**6]).astype(int))


# In[ ]:


data.retweets = (data.retweets.replace(r'[KM]+$', '', regex=True).astype(float) *           data.retweets.str.extract(r'[\d\.]+([KM]+)', expand=False)
            .fillna(1)
            .replace(['K','M'], [10**3, 10**6]).astype(int))


# In[ ]:


data.replies = (data.replies.replace(r'[KM]+$', '', regex=True).astype(float) *           data.replies.str.extract(r'[\d\.]+([KM]+)', expand=False)
            .fillna(1)
            .replace(['K','M'], [10**3, 10**6]).astype(int))


# In[ ]:


data


# In[ ]:


data['Video'] = data['Video'].replace({True: 1, False: 0})

data['pinned'] = data['pinned'].replace({True: 1, False: 0})

data['retweeted'] = data['retweeted'].replace({True: 1, False: 0})


# In[ ]:


data


# In[ ]:


data.to_csv('Your_CSV_clean.csv') 

