# 🌸 KNN Iris Classifier

This project demonstrates a basic **K-Nearest Neighbors (KNN)** algorithm implementation using the **Iris dataset**. It evaluates model accuracy for different values of **K (from 1 to 10)** and visualizes the relationship between K and model accuracy.

---

## 📂 Project Files

- `main.py` – Main script that trains and evaluates the KNN model
- `accuracy_vs_k.png` – A plot showing K values vs. their corresponding accuracy scores
- `README.md` – Project description and instructions (this file)

---

## 📊 Dataset Info

- **Dataset**: Iris flower dataset (available in `scikit-learn`)
- **Features**:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- **Classes**:
  - Setosa (0)
  - Versicolour (1)
  - Virginica (2)

---

## 🧠 Model Details

- **Algorithm**: K-Nearest Neighbors (KNN)
- **Library Used**: `scikit-learn`
- **Evaluation Metric**: Accuracy
- **K values tested**: 1 to 10

---

## 📈 Output Example

The program trains the model for each K from 1 to 10 and prints the corresponding accuracy:


It also saves a graph: `accuracy_vs_k.png` 


## ▶️ How to Run

### 1. Install dependencies

```bash
pip install scikit-learn matplotlib
### 2.Run
python Knn_iris.py

