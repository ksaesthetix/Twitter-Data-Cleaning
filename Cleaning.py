import pandas as pd 

data = pd.read_csv('FoxNEws2018-2019.csv')

data['content'] = data['content'].str.replace(r'\W', " ")

data['retweets'] = (data['retweets'].replace(r'[KM]+$', '', regex=True).astype(float) * \
   ....:           data['retweets'].str.extract(r'[\d\.]+([KM]+)', expand=False)
   ....:             .fillna(1)
   ....:             .replace(['K','M'], [10**3, 10**6]).astype(int))

data['replies'] = (data['replies'].replace(r'[KM]+$', '', regex=True).astype(float) * \
   ....:           data['replies'].str.extract(r'[\d\.]+([KM]+)', expand=False)
   ....:             .fillna(1)
   ....:             .replace(['K','M'], [10**3, 10**6]).astype(int))

data['likes'] = (data['likes'].replace(r'[KM]+$', '', regex=True).astype(float) * \
   ....:           data['likes'].str.extract(r'[\d\.]+([KM]+)', expand=False)
   ....:             .fillna(1)
   ....:             .replace(['K','M'], [10**3, 10**6]).astype(int))

    
data['Video'] = data['Video'].replace({True: 1, False: 0})

data['pinned'] = data['pinned'].replace({True: 1, False: 0})

data['retweeted'] = data['retweeted'].replace({True: 1, False: 0})

data['Sentiment'] = data['Sentiment'].replace({'positive': 1, 'negative': -1, 'neutral': 0})

data.to_csv('FoxNews2018-2019Cleaned.csv') 




   
    
    
    
    