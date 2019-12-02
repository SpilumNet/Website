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

        account = db.con.execute("SELECT * FROM users WHERE username = %s AND passwd = %s", (username, password))

        for a in account:
            if a:
                session['loggedin'] = True
                session['id'] = a['id']
                session['username'] = a['username']
                session['email'] = a['email']

                return redirect(url_for('account.profile', user=username))
            else:
                msg = 'Incorrect username/password!'
    return render_template('modules/account/login.html', msg=msg)


@bp.route('/account/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('email', None)

    return redirect(url_for('account.login'))


@bp.route('/account/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form \
            and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        account = db.con.execute("SELECT * FROM users WHERE username = %s", username)
        acc = False
        for a in account:
            acc = True
            if a:
                msg = 'Account already exists!'

        if not acc:
            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address!'
            elif not re.match(r'[A-Za-z0-9]', username):
                msg = 'Username must only contain alphanumeric characters!'
            elif not username or not password or not email:
                msg = 'Please fill out the form!'
            else:
                db.con.execute(
                    "INSERT INTO users(username, passwd, email) SELECT %s, %s, %s", (username, password, email)
                )
                db.con.connection.commit()
                msg = 'You have successfully registered!'

    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template('modules/account/register.html', msg=msg)


@bp.route('/account/profile/<user>', methods=['GET', 'POST'])
def profile(user):
    msg = ''
    if request.method == 'POST' and 'comment' in request.form and session['username']:
        comment = request.form['comment']
        username = user
        author = session['username']
        db.con.execute(
            "INSERT INTO comments(message, username, author) SELECT %s, %s, %s", (comment, username, author)
        )
        db.con.connection.commit()
        msg = 'Comment submitted!'

    comments = db.con.execute(
        "SELECT * FROM comments WHERE username = %s", user
    )
    return render_template('modules/account/profile.html', user=user, comments=comments, msg=msg)


@bp.route('/comment/<id>/delete')
def del_comment(id):
    msg = ''
    user = session['username']
    comment = db.con.execute(
        "SELECT * FROM comments WHERE id = %s", id
    )
    try:
        if user and user == comment.fetchone().username:
            db.con.execute(
                "DELETE FROM comments WHERE id = %s", id
            ).fetchone()
            msg = 'Comment successfully deleted!'
        else:
            msg = 'You lack permission to delete that comment!'
    except:
        pass
    return redirect(url_for('account.profile', user=user, msg=msg))


@bp.route('/account/profile/list')
def list():
    users = db.con.execute(
        "SELECT username, email FROM users"
    )
    return render_template('modules/account/list.html', users=users)