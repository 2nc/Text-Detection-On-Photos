from flask import render_template, redirect, url_for, request, g
from app import webapp

import mysql.connector

from app.config import db_config


def connect_to_database():
    return mysql.connector.connect(user=db_config['user'],
                                   password=db_config['password'],
                                   host=db_config['host'],
                                   database=db_config['database'])


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db


@webapp.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@webapp.route('/GetData', methods=['GET'])
def getData():
    cnx = get_db()
    cursor = cnx.cursor()
    query = "SELECT * FROM user_information;"
    cursor.execute(query)
    print(cursor.rowcount)
    return render_template("GetData.html", cursor=cursor)
