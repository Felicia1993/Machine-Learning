# import libraries


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score



companies = pd.read_csv('1000_Companies.csv')
X = companies.iloc[:, :-1].values
y = companies.iloc[:, 4].values
# print(companies.head())
sns.heatmap(companies.corr(numeric_only=True))
plt.show()

labelEncoder = LabelEncoder()
X[:,3] = labelEncoder.fit_transform(X[:, 3])

hot_encoder = ColumnTransformer([('encoder', OneHotEncoder(), [3])], remainder='passthrough')

# hot_encoder = OneHotEncoder(categorical_features=[3])
X = hot_encoder.fit_transform(X)
#
# Avoid Dummy variable trap
X = X[:,1:]

# Fitting multiple linear regression model to training set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regression = LinearRegression()
regression.fit(X_train, y_train)

# Predicting the test result
y_predict = regression.predict(X_test)
# print(y_predict)

#caculating the coeffients
# print(regression.coef_)

#calculating the intercept
print(regression.intercept_)

#calculating the R square model
score = r2_score(y_test, y_predict)
print(score)





