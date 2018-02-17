import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import IPython
import sklearn
import mglearn


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifierfrom
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

df_test = pd.DataFrame(pd.read_csv('test_data.csv', na_values=['?']))

X_train = df.loc[:, :'thal']
y_train = df.loc[:, 'num':'num']

print('X_train: \n', X_train.keys(), '\ny_train: \n', y_train.keys(),
      X_train.shape, y_train.shape)


grr = pd.plotting.scatter_matrix(X_train, c=y_train['num'], figsize=(30, 30), hist_kwds={'bins': 30}, s=60, alpha=.6)


df = pd.DataFrame(pd.read_csv('train_data.csv', na_values=['?']))

df.hist()


# No NA
noNA_df = df.dropna()
noNA_df.shape


# with fill NA
fillNA_df = df.fillna(df.median())
fillNA_df.hist()

fillNA_df_test = df_test.fillna(df_test.median())


X_train_fillNA = fillNA_df.loc[:, :'thal']
y_train_fillNA = fillNA_df.loc[:, 'num':'num'].values.ravel()

X_test_fill_NA = fillNA_df_test.loc[:, :'thal']
y_test_fillNA = fillNA_df_test.loc[:, 'num':'num'].values.ravel()

forest = RandomForestClassifier(n_estimators=40, random_state=0)
forest.fit(X_train_fillNA, y_train_fillNA)

forest.score(X_train_fillNA, y_train_fillNA)
forest.score(X_test_fill_NA, y_test_fillNA)

plot_feature_importances(forest)
