import pandas as pd


df = pd.read_csv('diabetes.csv')

y = df.Outcome
X = df.drop('Outcome', axis='columns')

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

scores = cross_val_score(DecisionTreeClassifier(), X, y, cv=5)
print(scores.mean())    #in ra tỉ lệ độ chính xác của 1 model riêng lẻ

from sklearn.ensemble import BaggingClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier

#tạo 1 ensemble model với bagging
bag_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(),   #phương pháp Decision Tree
    n_estimators=100,   #tạo 100 weak learners
    max_samples=0.8,    #tỉ lệ tối đa số samples được lấy
    oob_score=True,     #cho phép testing với các mẫu không xuất hiện ở Bootstraped Dataset nào
    random_state=0
)
scores = cross_val_score(bag_model, X, y, cv=5)
print(scores.mean())


