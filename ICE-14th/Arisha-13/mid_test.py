from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt

# Load dataset
X, y = load_digits(return_X_y=True)

# Split dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Print dataset information
print("Total Data:", len(X))
print("Training Data:", len(X_train))
print("Testing Data:", len(X_test))

# Train SVM model
model = SVC(kernel='rbf')
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display accuracy
print("Accuracy:", accuracy)
print("Accuracy (%):", accuracy * 100, "%")

# Confusion Matrix
ConfusionMatrixDisplay(
    confusion_matrix(y_test, y_pred)
).plot()

plt.show()