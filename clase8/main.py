from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


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
    if 'active' in session:
        return render_template('dashboard.html')
    return redirect('/')

@app.route('/check-user', methods=['POST'])
def create_user():
    users = [
        {'name' : 'John Shelby', 'email' : 'john@shelby.com' , 'password' : 'johnshelby'},
        {'name' : 'Tommy Shelby', 'email' : 'tommy@shelby.com' , 'password' : 'tommyshelby'},
        {'name' : 'Arthur Shelby', 'email' : 'arthur@shelby.com' , 'password' : 'arthurshelby'},
        {'name' : 'Finn Shelby', 'email' : 'finn@shelby.com' , 'password' : 'finnshelby'},
        {'name' : 'Michael Gray', 'email' : 'michael@gray.com' , 'password' : 'michaelgray'},
    ]

    for user in users:
        if user['email'] == request.form['email'] and user['password'] == request.form['pass']:
            session['name'] = user['name']
            session['active'] = True
            return redirect('/panel')
    flash('Error en Email o Clave')
    return redirect("/ingresar")	

@app.route('/salir')
def logout():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)
