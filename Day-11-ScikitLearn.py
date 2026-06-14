# ==========================================
# STEP 1 : IMPORT LIBRARIES
# ==========================================

from sklearn.datasets import load_iris
from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)

from sklearn.preprocessing import StandardScaler

from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# ==========================================
# STEP 2 : LOAD DATASET
# ==========================================

iris = load_iris()

X = iris.data
y = iris.target

print("Dataset Shape:", X.shape)

# ==========================================
# STEP 3 : TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# ==========================================
# STEP 4 : PIPELINE
# ==========================================

pipeline = Pipeline([

    ("scaler", StandardScaler()),

    ("model", LogisticRegression())

])

# ==========================================
# STEP 5 : TRAIN MODEL
# ==========================================

pipeline.fit(X_train, y_train)

print("\nModel Training Completed")

# ==========================================
# STEP 6 : PREDICTIONS
# ==========================================

y_pred = pipeline.predict(X_test)

print("\nPredictions:")
print(y_pred)

# ==========================================
# STEP 7 : ACCURACY
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

# ==========================================
# STEP 8 : CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# ==========================================
# STEP 9 : CLASSIFICATION REPORT
# ==========================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred
    )
)

# ==========================================
# STEP 10 : CROSS VALIDATION
# ==========================================

scores = cross_val_score(
    pipeline,
    X,
    y,
    cv=5
)

print("\nCross Validation Scores:")
print(scores)

print("\nAverage CV Score:")
print(scores.mean())

# ==========================================
# STEP 11 : OVERFITTING CHECK
# ==========================================

train_accuracy = pipeline.score(
    X_train,
    y_train
)

test_accuracy = pipeline.score(
    X_test,
    y_test
)

print("\nTraining Accuracy:")
print(train_accuracy)

print("\nTesting Accuracy:")
print(test_accuracy)

# ==========================================
# STEP 12 : SIMPLE ANALYSIS
# ==========================================

difference = train_accuracy - test_accuracy

print("\nDifference:")
print(difference)

if difference > 0.10:
    print("\nPossible Overfitting")

elif train_accuracy < 0.70 and test_accuracy < 0.70:
    print("\nPossible Underfitting")

else:
    print("\nModel Looks Reasonable")