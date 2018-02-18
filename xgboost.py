import numpy as np
import pandas as pd
import xgboost as xgb
import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV


# load data from .csv
df_train = pd.DataFrame(pd.read_csv('train_data.csv', na_values=['?']))
df_test = pd.DataFrame(pd.read_csv('test_data.csv', na_values=['?']))

# fill NA
fillNA_train = df_train.fillna(df_train.median())
fillNA_test = df_test.fillna(df_test.median())

# data split
X_train, X_test, y_train, y_test = train_test_split(fillNA_train.loc[:, :'thal'],
                                                    fillNA_train.loc[:, 'num':'num'], test_size=0)


X_test, some_fake, y_test, another_fake = train_test_split(fillNA_test.loc[:, :'thal'],
                                                           fillNA_test.loc[:, 'num':'num'], test_size=0)

# sklearn-like interface
#xgbc = xgb.XGBClassifier(learning_rate=0.05, n_estimators=50, max_depth=4, n_jobs=-1)
xgbc = xgb.XGBClassifier(n_jobs=-1)

xgbc.fit(X_train, y_train)

xgbc.score(X_train, y_train)
xgbc.score(X_test, y_test)

xgb.plot_importance(xgbc)

#xgb.plot_tree(xgbc)     # не пашет у меня

# grid search
parm_grid = {'learning_rate': [0.01, 0.05, 0.1, 0.2],
             'n_estimators': [10, 30, 50, 70, 100, 150],
             'max_depth': [1, 2, 3, 4, 5, 7, 10]}

grid = GridSearchCV(xgb.XGBClassifier(), param_grid=parm_grid)
grid.fit(X_train, y_train)

grid.best_params
grid.best_score

grid.score(X_test, y_test)


