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


@webapp.route('/register', methods=['GET', 'POST'])
def register():
    uname_r = None
    e_r = None

    if 'username_r' in session:
        uname_r = session['username_r']

    if 'error_r' in session:
        e_r = session['error_r']

    return render_template("register.html", error=e_r, username=uname_r)


@webapp.route('/register_submit', methods=['POST'])
def register_submit():
    cnx = get_db()
    cursor = cnx.cursor()
    if 'username' in request.form and \
            'password' in request.form and 'confirm_password' in request.form:
        query = "SELECT * FROM user_information WHERE username='%s';" % (request.form['username'])
        cursor.execute(query)
        c = cursor.fetchall()
        # Judge if the username has duplicate
        if len(c) == 1 and c[0][0] == request.form['username']:
            session['error_r'] = "This user had registered, change another username!"
            return redirect(url_for('register'))
        # Judge whether the two passwords are same
        if request.form['password'] != request.form['confirm_password']:
            session['error_r'] = "The two passwords are not the same, please confirm!"
            return redirect(url_for('register'))
        query = "INSERT INTO user_information VALUES ('%s','%s');" % (
        request.form['username'], request.form['password'])
        try:
            cursor.execute(query)
            cnx.commit()
        except:
            # 发生错误时回滚
            cnx.rollback()

        success = "Create account Success, please login!"
        return render_template("login.html", register_success=success)

    session['error_r'] = "Every box should have value!"
    return redirect(url_for('register'))


@webapp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('main'))
