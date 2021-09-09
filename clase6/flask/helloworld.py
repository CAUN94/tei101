from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/template')
def hello_template():
    return render_template('index.html')

@app.route('/bye')
def bye():
    return 'Bye World!'

@app.route('/template_variable')
def hello_template_variable():
    return render_template(
        'variables.html',
        name = "Cristóbal",
        age=26,
        times = 10
        )

@app.route('/hello/<name>')
def hello_name(name):
    return "Hello "+name

@app.route('/hello/<name>/<lastname>')
def hello_name_lastname(name,lastname):
    return "Hello "+name+" "+lastname


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    return render_template(
        "show.html",
        name_on_template=name_from_form,
        email_on_template=email_from_form
    )




if __name__=="__main__":
    app.run(debug=True)
