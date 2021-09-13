# -*- coding: utf-8 -*-
"""Santander_project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aovpCzyMUkDhKyjmokM4f1wvrCOhSoEs

# **Santander Customer Transaction Prediction**

**Introduction :**

In this project we have to identify which customers will make a specific transaction in the future, irrespective of the amount of money transacted.
"""

# Import all required libraries 
import numpy as np
import pandas as pd

import seaborn as sns
from matplotlib import pyplot as plt

from sklearn.model_selection import train_test_split

import lightgbm as lgb

#Loading test and train datasets
df_train=pd.read_csv("train.csv")
df_test=pd.read_csv("test.csv")

#Checking the train data
df_train.head(2)

df_train.shape

#Checking data type
df_train.dtypes.value_counts()

df_train.describe()

"""**Exploratory data analysis**"""

#Checking null values
df_train.isnull().values.any(),    df_test.isnull().values.any()

# Checking if every row has unique id
len(df_train['ID_code'].unique())

#Target column
df_train['target'].value_counts()

sns.countplot(df_train.target)
print('% of 1 in train data:', (df_train.target.value_counts()[1]/df_train.shape[0]) * 100)



"""We have imbalance data"""

#Removing the ID_code column from the train dataset

new_train=df_train.drop(['ID_code'], axis=1)
new_train.head(2)

"""**SMOTE**"""

# Using SMOTE for balancing the target column in train dataset

from imblearn.over_sampling import SMOTE

print(new_train.target.value_counts())

X = new_train.drop('target', axis=1)
Y = new_train['target']

sm = SMOTE(random_state=42)
X_res, Y_res = sm.fit_resample(X, Y)

df_smote_over = pd.concat([pd.DataFrame(X_res), pd.DataFrame(Y_res, columns=['target'])], axis=1)

print('SMOTE over-sampling:')
print(df_smote_over.target.value_counts())

df_smote_over.target.value_counts().plot(kind='bar', title='Count (target)');



"""**Outliers**"""

#As the data is huge, we will first calculate the z-score of the training data
from scipy import stats

# Dropping ID and target columns
z_score_calc = df_train.drop(columns=['ID_code', 'target'])
# Calculating z score
z = np.abs(stats.zscore(z_score_calc))
# print(z)
threshold = 3
print(np.where(z > 4))

"""first array shows row number

second array shows coulmn number
"""

treated_data = df_train[(z < 4).all(axis=1)]
print("before treating outliers : {}".format(df_train.shape))
print("after treating outliers : {}".format(treated_data.shape))

"""There are total 27 outliers rows that are removed


"""



"""**Creating LightGBM Model**"""

var_columns = [c for c in df_train.columns if c not in ['ID_code','target']]

X = df_train.loc[:,var_columns]
y = df_train.loc[:,'target']

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2)
X_train.shape, X_valid.shape, y_train.shape, y_valid.shape

train_data = lgb.Dataset(X_train, label=y_train)
valid_data = lgb.Dataset(X_valid, label=y_valid)

parameters = {'objective': 'binary',
              'metric': 'auc',
              'is_unbalance': 'true',
              'boosting': 'gbdt',
              'num_leaves': 63,
              'feature_fraction': 0.5,
              'bagging_fraction': 0.5,
              'bagging_freq': 20,
              'learning_rate': 0.01,
              'verbose': -1
             }

model_lgbm = lgb.train(parameters,
                            train_data,
                            valid_sets=valid_data,
                            num_boost_round=5000,
                            early_stopping_rounds=50)

y_train_pred = model_lgbm.predict(X_train)
y_valid_pred = model_lgbm.predict(X_valid)

print("AUC Train: {:.4f}\nAUC Valid: {:.4f}".format(roc_auc_score(y_train, y_train_pred),
                                                    roc_auc_score(y_valid, y_valid_pred)))

"""Predicting the test data"""

df_test = pd.read_csv('test.csv')
df_sample_submission = pd.read_csv('sample_submission.csv')

X_test = df_test.loc[:,var_columns]
df_sample_submission['target'] = model_lgbm.predict(X_test)
df_sample_submission





