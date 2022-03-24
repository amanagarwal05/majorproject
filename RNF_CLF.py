#!/usr/bin/env python
# coding: utf-8

# # IMPORTING DATASETS

# In[95]:


import pandas as pd
train_df_10 = pd.read_csv("NSLKDD_top_10_TRAIN.csv")
test_df_10 = pd.read_csv("NSLKDD_top_10_TEST.csv")


# In[96]:


train_df_10


# In[97]:


test_df_10


# # SPLITTING THE DATASET

# In[98]:


train_df_15 = pd.read_csv("NSLKDD_top_15_TRAIN.csv")
test_df_15 = pd.read_csv("NSLKDD_top_15_TEST.csv")


# In[99]:


train_df_6 = pd.read_csv("NSLKDD_top_6_TRAIN.csv")
test_df_6 = pd.read_csv("NSLKDD_top_6_TEST.csv")


# In[100]:


train_x_10 = train_df_10.drop(labels=['attack'],axis=1)
train_y_10 = train_df_10['attack']


# In[101]:


test_x_10 = test_df_10.drop(labels=['attack'],axis=1)
test_y_10 = test_df_10['attack']


# In[102]:


train_x_15 = train_df_15.drop(labels=['attack'],axis=1)
train_y_15 = train_df_15['attack']


# In[103]:


test_x_15 = test_df_15.drop(labels=['attack'],axis=1)
test_y_15 = test_df_15['attack']


# In[104]:


train_x_6 = train_df_6.drop(labels=['attack'],axis=1)
train_y_6 = train_df_6['attack']


# In[105]:


test_x_6 = test_df_6.drop(labels=['attack'],axis=1)
test_y_6 = test_df_6['attack']


# # HYPER-PARAMETER TUNING USING RANDOMIZED SEARCH

# In[107]:


from sklearn.model_selection import RandomizedSearchCV
param_grid = {
    "n_estimators":[100,120,150,170,200], 
    "criterion":["gini","entropy"], 
    "max_features":["auto","sqrt","log2"], 
    "min_samples_leaf":range(1,10,1), 
    "min_samples_split":range(2,10,1)
}


# In[108]:


from sklearn.ensemble import RandomForestClassifier
#ran_search = RandomizedSearchCV(estimator=RandomForestClassifier(),param_distributions=param_grid,cv=5,n_jobs=-1)


# In[109]:


#ran_search.fit(train_x_10,train_y_10)


# In[110]:


#print(f'for Top 10 features: {ran_search.best_params_}')


# In[111]:


#ran_search.fit(train_x_15,train_y_15)


# In[112]:


#print(f'for Top 15 features: {ran_search.best_params_}')


# In[113]:


#ran_search.fit(train_x_6,train_y_6)


# In[114]:


#print(f'for Top 6 features: {ran_search.best_params_}')


# # CREATING MODELS FOR TOP 6 10 AND 15 FEATURES USING THE RANDOMIZED SEARCH VALUES

# In[121]:


#clf_10 = RandomForestClassifier(n_estimators=150,min_samples_split=7,min_samples_leaf=2,max_features="log2",criterion="entropy")
#clf_10.fit(train_x_10,train_y_10)


# In[122]:


from sklearn.metrics import classification_report,accuracy_score
#ypred_10 = clf_10.predict(test_x_10)
#print(f'top_10{classification_report(test_y_10,ypred_10)}')


# In[123]:


#clf_15 = RandomForestClassifier(n_estimators=170,min_samples_split=5,min_samples_leaf=2,max_features="auto",criterion="entropy")
#clf_15.fit(train_x_15,train_y_15)


# In[124]:


#ypred_15 = clf_15.predict(test_x_15)
#print(f'top_15{classification_report(test_y_15,ypred_15)}')


# In[125]:


clf_6 = RandomForestClassifier(n_estimators=200,min_samples_split=9,min_samples_leaf=4,max_features="log2",criterion="gini")
clf_6.fit(train_x_6,train_y_6)


# In[126]:


ypred_6 = clf_6.predict(test_x_6)
print(f'top_6{classification_report(test_y_6,ypred_6)}')


# In[ ]:





# In[ ]:





# In[ ]:




