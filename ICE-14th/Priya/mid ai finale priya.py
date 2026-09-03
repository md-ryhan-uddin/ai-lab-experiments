from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay

X,y=load_digits(return_X_y=True)
X1,X2,y1,y2=train_test_split(X,y,test_size=0.2,random_state=42)

m=KNeighborsClassifier()
m.fit(X1,y1)
p=m.predict(X2)

print("Accuracy:",accuracy_score(y2,p))
ConfusionMatrixDisplay.from_predictions(y2,p)
import matplotlib.pyplot as plt
plt.show()