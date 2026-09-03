import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

# Load Iris Dataset
data=load_iris(as_frame=True)
X=data.data
y=data.target

# Train-Test Split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

print("="*60)
print("EXPERIMENT 4(2): Gaussian Naive Bayes and SVM on Iris Dataset")
print("="*60)

# Gaussian Naive Bayes
print("\n--- Gaussian Naive Bayes ---")
nb=GaussianNB()
nb.fit(X_train,y_train)
y_pred_nb=nb.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test,y_pred_nb):.4f}")
print("\nClassification Report:")
print(classification_report(y_test,y_pred_nb,target_names=data.target_names))
disp=ConfusionMatrixDisplay(confusion_matrix(y_test,y_pred_nb),display_labels=data.target_names)
disp.plot(cmap="Blues")
plt.title("Gaussian Naive Bayes - Confusion Matrix")
plt.show()

print("\nLearned Class Prior Probabilities:")
print(nb.class_prior_)
print("\nLearned Means:")
print(nb.theta_)

# Support Vector Machine
print("\n--- Support Vector Machine (SVM) ---")
svm=SVC(kernel="linear",C=1.0)
svm.fit(X_train,y_train)
y_pred_svm=svm.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test,y_pred_svm):.4f}")
print("\nClassification Report:")
print(classification_report(y_test,y_pred_svm,target_names=data.target_names))
disp=ConfusionMatrixDisplay(confusion_matrix(y_test,y_pred_svm),display_labels=data.target_names)
disp.plot(cmap="Greens")
plt.title("Support Vector Machine - Confusion Matrix")
plt.show()

kernels=["linear","rbf","poly","sigmoid"]
acc=[]
for k in kernels:
    model=SVC(kernel=k,C=1.0,gamma="scale")
    model.fit(X_train,y_train)
    pred=model.predict(X_test)
    a=accuracy_score(y_test,pred)
    acc.append(a)
    print(f"{k.upper()} Kernel Accuracy: {a:.4f}")

plt.figure(figsize=(6,4))
plt.plot(kernels,acc,marker="o")
plt.title("SVM Accuracy for Different Kernels")
plt.xlabel("Kernel")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()

# Comparison
models=["Naive Bayes","SVM"]
scores=[accuracy_score(y_test,y_pred_nb),accuracy_score(y_test,y_pred_svm)]
plt.figure(figsize=(5,4))
plt.bar(models,scores)
plt.ylim(0.8,1.05)
plt.title("Accuracy Comparison: Naive Bayes vs SVM")
plt.ylabel("Accuracy")
plt.show()
