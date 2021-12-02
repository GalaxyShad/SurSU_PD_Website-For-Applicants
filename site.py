from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

site = Flask(__name__)
site.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test.db'
db = SQLAlchemy(site)


@site.route('/')
@site.route('/home')
def index():
    return render_template("index.html")


# @site.route('/about')
# def about():
#     return render_template("about.html")


# @site.route('/user/<string:name>/<int:id>')
# def user(name, id):
#     return "User page: " + name + " - " + str(id)


if __name__ == "__main__":
    site.run(debug=True)
