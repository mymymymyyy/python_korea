import matplotlib.pyplot
import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
print(sklearn.__version__)

선형기계학습 = LinearRegression()

원본데이터 = pd.read_csv('kyobo.csv',encoding='cp949')
print(원본데이터.head())

X = 원본데이터.iloc[:,:-1].values
y = 원본데이터.iloc[:,-1].values

선형기계학습.fit(X,y)


y_pred = 선형기계학습.predict(X)



print('예측한 y값\n',y_pred)
print('AI예측값',선형기계학습.predict([[300]]))
print('AI예측값',선형기계학습.predict([[6.5],[9]]))

plt.scatter(X,y,color='green')
plt.plot(X, y_pred, color='red') 
plt.title('title')
plt.xlabel('xtitle')
plt.ylabel('ytitle')
plt.show() 