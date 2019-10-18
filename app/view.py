import boto3
from flask import render_template, request, session, redirect, url_for, escape

from app import config
from app import webapp
from app.user_op_data import get_db, ServerError


@webapp.route('/view', methods=['POST', 'GET'])
def view():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = str(session['username'])
    cnx = get_db()
    cursor = cnx.cursor()

    query = "SELECT origin_path,thumb_path,text_path from user_information,image where image.user_id = user_information.user_id and username = '%s';" % username
    cursor.execute(query)
    allphotos = cursor.fetchall()
    if not allphotos:
        session['error_dis'] = "No photo in your account, Please upload photos first!"
        return redirect(url_for('disPhoto'))
    for row in allphotos:
        print(row[1])
    return render_template('view.html', allphotos=allphotos)
