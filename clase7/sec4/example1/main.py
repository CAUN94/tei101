from flask import Flask, render_template, request
app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return render_template('index.html')

@app.route('/calculo', methods=['POST'])          
def calculo():
    nr1 = int(request.form['nr1'])
    a = request.form['a']
    nr2 = int(request.form['nr2'])
    result = 'Error'
    if a == '+':
        result = nr1 + nr2
    elif a == '-':
        result = nr1 - nr2
    elif a == '*':
        result = nr1 * nr2
    elif a == '/':
        result = nr1 / nr2
    elif a == '**':
        result = nr1 ** nr2
    return render_template(
        'calculo.html',
        nr1 = nr1,
        a = a,
        nr2 = nr2,
        result = result
    )

if __name__=="__main__":   
    app.run(debug=True)    
