#!/usr/bin/env python
# coding: utf-8

# # PREPROCESSING TRAINING DATA

# In[1]:


import pandas as pd
train_full_df = pd.read_csv("NSLKDD_TRAIN.csv")
train_full_df


# In[2]:


train_full_df.isnull().sum()


# In[3]:


train_full_df.dtypes


# In[4]:


train_full_df['attack'].value_counts()


# In[5]:


train_full_df['protocol_type'].value_counts()                   


# In[6]:


train_full_df['service'].value_counts() 


# In[7]:


train_full_df['flag'].value_counts() 


# In[8]:


attack_types = {
    "back":"DOS",
    "land":"DOS",
    "neptune":"DOS",
    "pod":"DOS",
    "smurf":"DOS",
    "teardrop":"DOS",
    "apache2":"DOS",
    "udpstorm":"DOS",
    "processtable":"DOS",
    "worm":"DOS",
    "satan":"PROBE",
    "ipsweep":"PROBE",
    "nmap":"PROBE",
    "portsweep":"PROBE",
    "mscan":"PROBE",
    "saint":"PROBE",
    "guess_passwd":"R2L",
    "ftp_write":"R2L",
    "imap":"R2L",
    "phf":"R2L",
    "multihop":"R2L",
    "warezmaster":"R2L",
    "warezclient":"R2L",
    "spy":"R2L",
    "xlock":"R2L",
    "xsnoop":"R2L",
    "snmpguess":"R2L",
    "snmpgetattack":"R2L",
    "httptunnel":"R2L",
    "sendmail":"R2L",
    "named":"R2L",
    "buffer_overflow":"U2R",
    "loadmodule":"U2R",
    "rootkit":"U2R",
    "perl":"U2R",
    "sqlattack":"U2R",
    "xterm":"U2R",
    "ps":"U2R",
    "mailbomb":"DOS",
    "normal":"NORMAL"
    
}


# In[9]:


train_full_df['attack']=train_full_df['attack'].map(attack_types)


# In[10]:


train_full_df['attack'].value_counts()  


# # LABEL ENCODING FOR THE TRAINING DATA

# In[11]:


from sklearn.preprocessing import LabelEncoder
cat_features =['protocol_type','service','flag','attack']
train_le = LabelEncoder()
for feature_name in cat_features:
    train_full_df[feature_name] = train_le.fit_transform(train_full_df[feature_name])
    print(f'Encoded classes for {feature_name} {train_le.classes_}')


# In[12]:


train_full_df['attack'].value_counts()


# In[13]:


import matplotlib.pyplot as plt
attack_summary = train_full_df['attack'].value_counts().to_frame()
attack_summary = attack_summary.reset_index()
attack_summary.rename(columns={'index':'attack_type','attack':'count'},inplace=True)
plt.bar(attack_summary['attack_type'],attack_summary['count'],color=['blue','red','green','orange','orange'])
plt.show()


# In[14]:


train_full_df


# # FEATURE SELECTION FOR TOP 10 BEST FEATURES

# In[15]:


IND_VAR = train_full_df.drop(labels=['attack'],axis=1).to_numpy()
DEP_VAR = train_full_df['attack'].to_numpy()


# In[16]:


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
ordered_rank_features = SelectKBest(score_func=f_classif,k=5)
ordered_features = ordered_rank_features.fit(IND_VAR,DEP_VAR)
ordered_features.scores_


# In[17]:


scores_df = pd.DataFrame(ordered_features.scores_,columns=['feature_score'])
ind_features = train_full_df.drop(labels=['attack'],axis=1)
features_df = pd.DataFrame(ind_features.columns,columns=['feature'])


# In[18]:


features_scores = pd.concat([features_df,scores_df],axis=1)
#features_scores.columns=['feature','feature_score']
features_scores


# In[19]:


top_10_features_df = features_scores.nlargest(10,'feature_score')
top_10_features_df


# In[20]:


top_15_features_df = features_scores.nlargest(15,'feature_score')
top_15_features = list(top_15_features_df['feature'])
top_15_features.append('attack')


# In[21]:


top_6_features_df = features_scores.nlargest(6,'feature_score')
top_6_features = list(top_6_features_df['feature'])
top_6_features.append('attack')


# In[22]:


top_10_features = list(top_10_features_df['feature'])
top_10_features.append('attack')
print(top_10_features)


# In[23]:


train_df_10=train_full_df[top_10_features]
train_df_10


# In[24]:


train_df_15=train_full_df[top_15_features]
train_df_15


# In[25]:


train_df_6=train_full_df[top_6_features]
train_df_6


# In[26]:


train_df_10.to_csv ("NSLKDD_top_10_TRAIN.csv", index=None)


# In[27]:


train_df_15.to_csv ("NSLKDD_top_15_TRAIN.csv", index=None)


# In[28]:


train_df_6.to_csv ("NSLKDD_top_6_TRAIN.csv", index=None)


# # PREPROCESSING TESTING DATA

# In[29]:


test_full_df = pd.read_csv("NSLKDD_Test.CSV")
test_full_df


# In[30]:


test_full_df.dtypes


# In[31]:


test_full_df.isnull().sum()


# In[32]:


test_full_df['attack'].value_counts()  


# In[33]:


test_full_df['protocol_type'].value_counts()  


# In[34]:


test_full_df['service'].value_counts()  


# In[35]:


test_full_df['flag'].value_counts()  


# In[36]:


test_full_df['attack'] = test_full_df['attack'].map(attack_types) 


# In[37]:


test_full_df['attack'].value_counts()  


# In[38]:


test_full_df


# # LABEL ENCODING FOR TESTING DATA

# In[39]:


test_le = LabelEncoder()
for feature_name in cat_features:
    test_full_df[feature_name] = test_le.fit_transform(test_full_df[feature_name])
    print(f'Encoded classes for {feature_name} {test_le.classes_}')


# In[40]:


test_full_df['attack'].value_counts()  


# In[41]:


test_full_df


# In[42]:


test_df_10 = test_full_df[top_10_features]
test_df_10


# In[43]:


test_df_15 = test_full_df[top_15_features]
test_df_15


# In[44]:


test_df_6 = test_full_df[top_6_features]
test_df_6


# In[45]:


train_df_10


# In[46]:


test_df_10


# In[47]:


test_df_10.to_csv ("NSLKDD_top_10_TEST.csv", index=None)


# In[48]:


test_df_15.to_csv ("NSLKDD_top_15_TEST.csv", index=None)


# In[49]:


test_df_6.to_csv ("NSLKDD_top_6_TEST.csv", index=None)


# In[50]:


DATAFRAME_train = pd.read_csv("NSLKDD_top_10_TRAIN.csv")
DATAFRAME_train


# In[51]:


DATAFRAME_test = pd.read_csv("NSLKDD_top_10_TEST.csv")
DATAFRAME_test


# In[52]:


attack_summary = test_full_df['attack'].value_counts().to_frame()
attack_summary = attack_summary.reset_index()
attack_summary.rename(columns={'index':'attack_type','attack':'count'},inplace=True)
plt.bar(attack_summary['attack_type'],attack_summary['count'],color=['blue','red','green','orange','orange'])
plt.show()


# In[53]:


train_df_10


# In[54]:


test_df_10


# In[ ]:




