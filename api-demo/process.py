import pandas as pd
import json

#read data.jsonl
data = []
with open('data.jsonl') as f:
    for line in f:
        data.append(json.loads(line))
print(data[:3])
df=pd.DataFrame(data)
print(df.head(3))
print(df['label_text'].value_counts())
print(df['label_text'].value_counts().index[:5])
top_5_labels = df['label_text'].value_counts().index[:5]
#extract all rows with top 5 labels
df_top_5 = df[df['label_text'].isin(top_5_labels)]
#split into train and test randomly
df_train = df_top_5.sample(frac=0.8, random_state=0)
df_test = df_top_5.drop(df_train.index)
df_train = df_train[['text', 'label_text']]
df_train.columns = ['text', 'label']
df_test = df_test[['text', 'label_text']]
df_test.columns = ['text', 'label']
print(df_train.shape, df_test.shape)
df_train.to_csv('train.csv', index=False)
df_test.to_csv('test.csv', index=False)
#create another train and test with the 6th label
df_6th = df[df['label_text']==df['label_text'].value_counts().index[5]]
print(df['label_text'].value_counts().index[5])
df_train_6th = df_6th.sample(frac=0.8, random_state=0)
df_test_6th = df_6th.drop(df_train_6th.index)
print(df_train_6th.shape, df_test_6th.shape)
df_train_6th = df_train_6th[['text', 'label_text']]
df_train_6th.columns = ['text', 'label']
df_test_6th = df_test_6th[['text', 'label_text']]
df_test_6th.columns = ['text', 'label']
df_train_6th.to_csv('train_6th.csv', index=False)
df_test_6th.to_csv('test_6th.csv', index=False)
