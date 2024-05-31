import pandas as pd
df=pd.read_csv('intent.csv')
print(df['INTENT_NAME'].value_counts().head())
most_common=['INFO_ADD_REMOVE_VEHICLE', 'INFO_LOGIN_ERROR',
       'INFO_ADD_REMOVE_INSURED', 'INFO_ERS', 'INFO_CAREERS',
       'INFO_DIFFERENT_AMTS', 'INFO_SPEAK_TO_REP', 'INFO_CANCEL_INS_POLICY',
       'INFO_UPDATE_LIENHOLDER', 'INFO_DELETE_DUPE_PYMT',
       'INFO_CANT_SEE_FARM_RANCH_POLICY', 'INFO_AUTO_INS_CANADA',
       'INFO_DEC_PAGE_NEEDED', 'INFO_LIFE_BENEFICIARY_CHANGE',
       'INFO_MAKE_PYMT',]

#extract 25 of each intent
df=df[df['INTENT_NAME'].isin(most_common)]
df=df.groupby('INTENT_NAME').head(25)

#split 20 of each into train and 2 of each to test
train=df.groupby('INTENT_NAME').head(3)
test=df.groupby('INTENT_NAME').tail(3)
# switch the order of columns
train=train[['UTTERANCES','INTENT_NAME']]
test=test[['UTTERANCES','INTENT_NAME']]
train.to_csv('train.csv',index=False,header=False)
test.to_csv('test.csv',index=False,header=False)