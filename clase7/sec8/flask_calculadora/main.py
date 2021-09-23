from flask import Flask, render_template, request
app = Flask(__name__)    




@app.route('/')          
def hello_world():
    return render_template('index.html')

@app.route('/calculadora', methods=['POST'])          
def calculator():
    print('--------------------------')
    print(request.form)
    nr1 = request.form['nr1']
    a = request.form['a']
    nr2 = request.form['nr2']
    if a == '+':
        result = int(nr1) + int(nr2)
    elif a == '-':
        result = int(nr1) - int(nr2)
    elif a == '*':
        result = int(nr1) * int(nr2)
    elif a == '/':
        result = int(nr1) / int(nr2)
    elif a == '**':
        result = int(nr1) ** int(nr2)
    return render_template(
            'result.html',
            nr1 = nr1,
            nr2 = nr2,
            a = a,
            result = result
        )





if __name__=="__main__":  
    app.run(debug=True)    

