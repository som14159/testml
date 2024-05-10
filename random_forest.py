import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('PlayTennis.csv')
y = df['Play Tennis']
X = df.drop(columns=['Play Tennis'])
X = pd.get_dummies(X)
model = RandomForestClassifier(n_estimators=10)
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.4)
print("hi")
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print("Accuracy Score:",accuracy_score(y_true=y_test,y_pred=y_pred))
for i in range(len(X.columns)):
    print(X.columns[i],"\t",model.feature_importances_[i])