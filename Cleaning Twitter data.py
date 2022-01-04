#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 


# In[ ]:


data = pd.read_csv('')


# In[ ]:


df = pd.DataFrame(data)


# In[ ]:


df = df.loc[:, df.columns.intersection(['created_at','user.screen_name','text','retweet_count','entities.media','favorite_count','favorited','retweeted','possibly_sensitive'])]


# In[ ]:


df


# In[ ]:


df['text'] = df['text'].str.replace(r'\W', " ")


# In[ ]:


df


# In[ ]:


df['favorited'] = df['favorited'].replace({True: 1, False: 0})

df['retweeted'] = df['retweeted'].replace({True: 1, False: 0})

df['possibly_sensitive'] = df['possibly_sensitive'].replace({True:1, False: 0})


# In[ ]:


df


# In[ ]:


df.to_csv('T') 

