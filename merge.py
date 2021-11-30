import pandas as pd 


# Formating first dataframe

df1 = pd.read_csv("old.csv")


lab = []

for index, row in df1.iterrows():

    if row['label'] == "REAL":

        lab.append(1)

    elif row['label'] == 'FAKE':

        lab.append(0)

df1['Label'] = lab

df1.drop(['label', "Unnamed: 0" ], axis = 1, inplace=True)

# Formating second dataframe

df2 = pd.read_csv("news.csv")

df2.drop(['URLs'], axis = 1, inplace=True)

df3 = df2.rename(columns = {'Headline': 'title', 'Body': 'text'}, inplace = False)

# Merging two DataFrames

frames = [df1, df3]
  
result = pd.concat(frames)

result.reset_index(drop = True, inplace = True)

print (result)

# Converting to a CSV

result.to_csv('result.csv', index = True)