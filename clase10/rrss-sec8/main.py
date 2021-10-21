from flask import Flask, render_template, request, session, redirect, flash, jsonify

app = Flask(__name__)
app.secret_key = 'Clave Segura'

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

@app.route('/registrarme')
def signin():
    return render_template('sign-up.html')

@app.route('/ingresar')
def signup():
    return render_template('sign-in.html')

@app.route('/registrar', methods=['POST'])
def register():
    if request.form['pass'] != request.form['cpass']:
        flash('Claves distintas')
        return redirect('/registrarme')

    users = users_gs.get_all_records()
    new_id = (users[0]['id']+1)

    row = [new_id,request.form['name'],request.form['email'],request.form['pass']]
    users_gs.insert_row(row,2)

    session['id'] = new_id
    session['name'] = request.form['name']
    session['active'] = True

    return redirect('/panel')

@app.route('/panel')
def panel():
    if 'active' in session:
        comments = comments_gs.get_all_records()
        users = users_gs.get_all_records()


        return render_template('panel.html', comments = comments, users = users)
    return redirect('/')
    

@app.route('/confirmar', methods=['POST'])
def login():
    users = users_gs.get_all_records()
    for user in users:
        if user['email'] == request.form['email'] and user['password'] == request.form['password']:
            session['id'] = user['id']
            session['name'] = user['name']
            session['active'] = True
            return redirect('/panel')
    flash('Error en Email o Clave')
    return redirect('/ingresar')


@app.route('/salir')
def logout():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)