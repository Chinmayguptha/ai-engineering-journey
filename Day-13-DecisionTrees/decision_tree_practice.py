from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


iris = load_iris()

X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = DecisionTreeClassifier()


model.fit(X_train, y_train)


predictions = model.predict(X_test)


accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)













from sklearn.tree import DecisionTreeClassifier

gini_model = DecisionTreeClassifier(
    criterion="gini"
)

entropy_model = DecisionTreeClassifier(
    criterion="entropy"
)

print("Gini Model Created")
print("Entropy Model Created")










from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))

plot_tree(
    model,
    filled=True
)

plt.show()



overfit_model = DecisionTreeClassifier(
    max_depth=None
)

overfit_model.fit(X_train, y_train)

print(
    "Training Accuracy:",
    overfit_model.score(X_train, y_train)
)

print(
    "Testing Accuracy:",
    overfit_model.score(X_test, y_test)
)


pruned_model = DecisionTreeClassifier(
    max_depth=3,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
)

pruned_model.fit(
    X_train,
    y_train
)

print(
    "Pruned Training Accuracy:",
    pruned_model.score(X_train, y_train)
)

print(
    "Pruned Testing Accuracy:",
    pruned_model.score(X_test, y_test)
)