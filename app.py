from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Генеруємо дані для навчання моделі
X_train = np.arange(1, 11).reshape(-1, 1)  # Перших 10 чисел Фібоначчі
y_train = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Відповідні значення

# Навчаємо модель на навчальних даних
model = LinearRegression()
model.fit(X_train, y_train)

@app.route("/")
def show_start_form():
    return render_template('form.html')

@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        number = int(request.form['number'])
        # Передаємо нове значення у модель для прогнозування
        prediction = model.predict([[number]])[0]
        return render_template('resultsform.html', number=number, predicted_number=int(prediction))
app.run()