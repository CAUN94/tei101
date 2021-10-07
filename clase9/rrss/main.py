import os
from flask import Flask, render_template, request, redirect, session, flash, jsonify

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

import gspread
from oauth2client.service_account import ServiceAccountCredentials

credential = ServiceAccountCredentials.from_json_keyfile_name("client.json",
                                                              ["https://spreadsheets.google.com/feeds",                                                               "https://www.googleapis.com/auth/spreadsheets",                                                        "https://www.googleapis.com/auth/drive.file",                                                        "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)
gsheet = client.open("tei101").sheet1

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
def check_user():
    users = gsheet.get_all_records()
    print(users)

    for user in users:
        if user['email'] == request.form['email'] and user['password'] == request.form['pass']:
            session['name'] = user['name']
            session['active'] = True
            return redirect('/panel')
    flash('Error en Email o Clave')
    return redirect("/ingresar")

@app.route('/register-user', methods=['POST'])
def register_user():
    users = gsheet.get_all_records()
    new_id = int(users[-1]['id'])+1
    # return jsonify(req)
    row = [new_id,request.form['name'],request.form['email'],request.form['pass']]
    gsheet.insert_row(row, 2)
    session['name'] = request.form['name']
    session['active'] = True
    return redirect('/panel')

@app.route('/salir')
def logout():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)
