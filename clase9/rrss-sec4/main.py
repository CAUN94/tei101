from flask import Flask, render_template, session, flash, request, redirect,jsonify

app = Flask(__name__)
app.secret_key = 'no revelar clave'

import gspread
from oauth2client.service_account import ServiceAccountCredentials

credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",
                                                              ["https://spreadsheets.google.com/feeds",                                                               "https://www.googleapis.com/auth/spreadsheets",                                                        "https://www.googleapis.com/auth/drive.file",                                                        "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)
users_gs = client.open("users").sheet1
comments_gs = client.open("comments").sheet1


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/excel')
def excel():
    return jsonify(users_gs.get_all_records())

@app.route('/nosotros')
def team():
    return render_template('team.html')

@app.route('/panel')
def panel():
    comments = comments_gs.get_all_records()
    users = users_gs.get_all_records()
    if 'active' in session:
        return render_template('panel.html', comments = comments,  users = users)
    return redirect('/')

@app.route('/registrarme')
def signup():
    return render_template('signup.html')

@app.route('/registrar', methods=['POST'])
def register():
    if request.form['pass'] != request.form['cpass']:
        flash('Claves no iguales')
        return redirect('/registrarme')
    users = users_gs.get_all_records()
    users_new_id = int(users[0]['id'] + 1)
    row = [users_new_id,request.form['name'],request.form['email'],request.form['pass']]
    users_gs.insert_row(row,2)

    session['id'] =  users_new_id
    session['name'] = request.form['name']
    session['active'] = True
    return redirect('/panel')


@app.route('/ingresar')
def signin():
    return render_template('signin.html')

@app.route('/salir')
def logout():
    session.clear()
    return redirect('/')

@app.route('/revisar', methods=['POST'])
def check():
    users = users_gs.get_all_records()

    for user in users:
        if user['email'] == request.form['email'] and user['password'] == request.form['password']:
            session['id'] = user['id']
            session['name'] = user['name']
            session['active'] = True
            return redirect('/panel')
    
    flash('Email o Clave erronea')
    return redirect('/ingresar')



if __name__=="__main__":
    app.run(debug=True)