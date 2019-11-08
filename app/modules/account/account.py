from flask import Blueprint, render_template, request, session, url_for, redirect
import re

from app import Database

db = Database()
bp = Blueprint('account', __name__)


@bp.route('/account/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        db.cur.execute("SELECT * FROM users WHERE user = %s AND pass = %s", (username, password))

        account = db.cur.fetchone()

        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['user']

            return redirect(url_for('account.profile'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('modules/account/login.html', msg=msg)


@bp.route('/account/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    return redirect(url_for('account.login'))


@bp.route('/account/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        db.cur.execute('SELECT * FROM users WHERE user = %s', username)
        account = db.cur.fetchone()

        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]', username):
            msg = 'Username must only contain alphanumeric characters!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            db.cur.execute('INSERT INTO users (user, pass, email) VALUES (%s, %s, %s)', (username, password, email))
            db.cur.connection.commit()
            msg = 'You have successfully registered!'

    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template('modules/account/register.html', msg=msg)


@bp.route('/account/profile')
def profile():
    if 'loggedin' in session:
        db.cur.execute('SELECT * FROM users WHERE id = %s', [session['id']])
        account = db.cur.fetchone()

        return render_template('modules/account/profile.html', account=account)

    return redirect(url_for('account.login'))
