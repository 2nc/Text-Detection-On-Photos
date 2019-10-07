from flask import render_template, session, request, redirect, url_for
from app import webapp
from app.user_op_data import get_db

webapp.secret_key = '\x80\xa9s*\x12\xc7x\xa9d\x1f(\x03\xbeHJ:\x9f\xf0!\xb1a\xaa\x0f\xee'


@webapp.route('/login', methods=['GET', 'POST'])
def login():
    uname = None
    e = None

    if 'username' in session:
        uname = session['username']

    if 'error' in session:
        e = session['error']

    return render_template("login.html", error=e, username=uname)


@webapp.route('/login_submit', methods=['POST'])
def login_submit():
    cnx = get_db()
    cursor = cnx.cursor()
    if 'username' in request.form and \
        'password' in request.form:
        query = "SELECT * FROM user_information WHERE username='%s';" % (request.form['username'])
        cursor.execute(query)
        c = cursor.fetchall()
        if len(c) == 1 and c[0][1] == request.form['password']:
            session['authenticated'] = True
            return redirect(url_for('disPhoto'))

    if 'username' in request.form:
        session['username'] = request.form['username']

    session['error'] = "Error! Incorrect username or password!"
    return redirect(url_for('login'))


@webapp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('main'))
