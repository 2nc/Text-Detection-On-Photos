from flask import render_template, url_for
from app import webapp


@webapp.route('/disPhoto')
def disPhoto():
    return render_template("disPhoto.html")