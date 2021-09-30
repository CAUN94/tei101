from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def team():
    return render_template('nosotros.html')

@app.route('/ingresar')
def signin():
    return render_template('sign-in.html')

@app.route('/registrarme')
def signup():
    return render_template('sign-up.html')

@app.route('/panel')
def dashboard():
    return render_template('dashboard.html')

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
