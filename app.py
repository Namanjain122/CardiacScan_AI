from flask import Flask, render_template, request
import numpy as np
import joblib
import pymysql

app = Flask(__name__)


# Load the trained decision tree model
decision_tree = joblib.load("decision3.pkl")

def insert_into_db(data):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Naman@1q2w',
        database='heart_db',
        cursorclass=pymysql.cursors.Cursor  # optional, default is fine too
    )
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO heart_data (
            age, gender, height, weight, ap_hi, ap_lo,
            cholesterol, gluc, smoke, alco, active,
            country, occupation
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', data)
    conn.commit()
    cursor.close()
    conn.close()

# Define the categories for encodmiing
countries = ['Indonesia', 'Malaysia', 'Singapore', 'India']
occupations = ['Architect', 'Accountant', 'Chef', 'Lawyer', 'Teacher', 'Nurse', 'Engineer', 'Doctor', 'Others']

# Function to encode categorical variables
def encode_category(value, category_list):
    return category_list.index(value) if value in category_list else len(category_list)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Get form data
            age = int(request.form["age"])
            gender = int(request.form["gender"])
            height = int(request.form["height"])
            weight = float(request.form["weight"])
            ap_hi = int(request.form["ap_hi"])
            ap_lo = int(request.form["ap_lo"])
            cholesterol = int(request.form["cholesterol"])
            gluc = int(request.form["gluc"])
            smoke = int(request.form["smoke"])
            alco = int(request.form["alco"])
            active = int(request.form["active"])
            country = request.form["country"]
            occupation = request.form["occupation"]

            # Encode categorical values
            country_encoded = encode_category(country, countries)
            occupation_encoded = encode_category(occupation, occupations)

            # Convert gender input (1 = Female, 2 = Male) to (0 = Female, 1 = Male)
            gender = 0 if gender == 1 else 1

            # Prepare input data
            user_data = np.array([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc,
                                   smoke, alco, active, country_encoded, occupation_encoded]])
            
            data = (
                age, gender, height, weight, ap_hi, ap_lo,
                cholesterol, gluc, smoke, alco, active,
                country, occupation
            )
            insert_into_db(data)

            # Make prediction
            prediction = decision_tree.predict(user_data)

            # Display result
            result = "You may have heart disease. Please consult a doctor." if prediction[0] == 1 else "No heart disease detected."

            return render_template("index.html", prediction=result)

        except ValueError:
            return render_template("index.html", prediction="Invalid input! Please enter valid numeric values.")

    return render_template("index.html", prediction=None)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
