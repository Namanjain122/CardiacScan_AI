# ❤️ CardiacScan AI Web Application

This project is a **Flask-based web application** that predicts the risk of heart disease based on user input using Machine Learning models. It also stores the submitted data into a MySQL database for record keeping or future analysis.

---

## 🚀 Features

- Predicts heart disease using trained ML models
- Accepts real-time user input via a web interface
- Stores user data into a MySQL database
- Categorical input support for country and occupation
- Displays results in a user-friendly format

---

## 🧠 Machine Learning Models Used

The model was trained using a cleaned and preprocessed dataset. Three supervised classification algorithms were compared and evaluated:

### 1. ✅ Decision Tree Classifier
- **Model Used in App**
- Simple and interpretable
- Can handle both numerical and categorical data
- Prone to overfitting, but performs well for structured datasets like this one

### 2. 🧪 Support Vector Machine (SVM)
- Trained using RBF kernel
- Good for binary classification problems
- Performs well on high-dimensional data
- Slower on large datasets

### 3. 📈 Logistic Regression
- Interpretable and easy to implement
- Performs well when classes are linearly separable
- Used as a benchmark model

**Evaluation Metric Used:**  
- Accuracy  
- Precision, Recall, F1-Score  
- Confusion Matrix

After comparison, the **Decision Tree model** was chosen for deployment due to its balance of accuracy and interpretability.

---

## 🧾 Input Features

The form collects the following inputs from the user:

- Age
- Gender (1 = Female, 2 = Male)
- Height (in cm)
- Weight (in kg)
- Systolic BP (`ap_hi`)
- Diastolic BP (`ap_lo`)
- Cholesterol (1-3)
- Glucose (1-3)
- Smoking (0 = No, 1 = Yes)
- Alcohol Intake (0 = No, 1 = Yes)
- Physical Activity (0 = No, 1 = Yes)
- Country (Drop-down)
- Occupation (Drop-down)

---

## 🗄️ Database Integration

User data is stored in a **MySQL database** called `heart_db`, in a table named `heart_data`.

```sql
CREATE TABLE heart_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    gender INT,
    height INT,
    weight FLOAT,
    ap_hi INT,
    ap_lo INT,
    cholesterol INT,
    gluc INT,
    smoke INT,
    alco INT,
    active INT,
    country VARCHAR(50),
    occupation VARCHAR(50)
);
