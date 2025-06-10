from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#Load dataset
iris = load_iris()
X = iris.data
Y = iris.target

#Split into training and testing
x_train,x_test,y_train,y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


accuracy_score_list=[]
K_value_list=[1,2,3,4,5,6,7,8,9,10]
#Train the model
#k value is ranging from 1 to 10
for k in range(1,11):
    model=KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    print(f"k = {k} ,Accuracy:",accuracy_score(y_test,y_pred))
    accuracy_score_list.append(accuracy_score(y_test,y_pred))

plt.plot(K_value_list, accuracy_score_list, marker='o', color='green')
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.title("K Value vs Accuracy")
plt.grid(True)
plt.xticks(K_value_list)
plt.savefig("accuracy_vs_k.png")
plt.show()

