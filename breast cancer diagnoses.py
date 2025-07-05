from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score , GridSearchCV 
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score , classification_report 

data = load_breast_cancer()
X = data.data
y = data.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC())])

parameters = { 'svm__C': [0.1, 1, 10] , 'svm__kernel': ['linear', 'rbf'],}

grid_search = GridSearchCV(pipe, parameters, cv=5)
grid_search.fit(X_train, y_train)

print("Best Parameters:", grid_search.best_params_)
print("Best Cross-Validation Score:", grid_search.best_score_)

# Test set evaluation
y_pred = grid_search.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test) 
print("Best Model Test Accuracy:", accuracy_score(y_test, y_pred_best))
print("Best Model Classification Report:\n", classification_report(y_test, y_pred_best))

accuracy = accuracy_score(y_test, y_pred_best) 
print("Final Test Accuracy:", accuracy)
# The code above implements a machine learning pipeline using SVM on the breast cancer dataset.
# It includes data preprocessing, hyperparameter tuning with grid search, and evaluation of 
# the model's performance on both the training and test sets.
# The final accuracy and classification report provide insights into the model's effectiveness in predicting breast cancer outcomes

classification_rep = classification_report(y_test, y_pred_best)
print("Classification Report:\n", classification_rep) 

cross_val_scores = cross_val_score(best_model, X, y, cv=5)
print("Cross-validation scores:", cross_val_scores) 
mean = cross_val_scores.mean()
print("Mean cross-validation score:", mean)