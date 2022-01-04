import pandas as pd 

data = pd.read_csv('')

df = pd.DataFrame(data)

df = df.loc[:, df.columns.intersection(['insert selection of columns'])]

df['text'] = df['text'].str.replace(r'\W', " ")

df['favorited'] = df['favorited'].replace({True: 1, False: 0})

df['retweeted'] = df['retweeted'].replace({True: 1, False: 0})

df['possibly_sensitive'] = df['possibly_sensitive'].replace({True:1, False: 0})

df.to_csv('T') 

