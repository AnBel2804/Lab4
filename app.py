from flask import Flask, render_template, request

app = Flask('flask1')

@app.route('/')
def show_start_form():
    return render_template('form.html')    
@app.route('/result', methods=['POST', 'GET'])
def result():
#    form=request.form 
    number = request.form['number']
    if number is not None:
        number = int(number)
        fib = lambda n: fib(n - 1) + fib(n - 2) if n > 1 else n
        predicted = fib(number)
        return render_template('resultsform.html', number=number, predicted_number=predicted)
    else:
        return "Number parameter is missing."

if __name__ == '__main__':
    app.run()