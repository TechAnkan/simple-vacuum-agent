from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split , cross_val_score
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score

iris = load_iris()
x= iris.data
y= iris.target
# print(iris)
# print(x)
# print(y)

X_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model = LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

y_pred = model.predict(x_test)
print("Predicted values:", y_pred)
accuracy= accuracy_score(y_test,y_pred)
print("Accuracy:", accuracy)

cross_val_scores = cross_val_score(model, x, y, cv=5)
print("Cross-validation scores:", cross_val_scores)

mean = cross_val_scores.mean()
print("Mean cross-validation score:", mean)

