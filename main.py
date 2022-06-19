from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder="static_files")
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:RRwed2003@localhost/web_db'
#db = SQLAlchemy(app)

"""
class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)

	def __init__(self, username, email):
		self.username = username
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.username


db.create_all()
print(User.query.all())
"""

header_urls_nav = {"Home": "/home", 
"Keyboards": "/keyboards", 
"Parts": "/parts", 
"Accessories": "/accessories", 
"Tools": "/tools"}


footer_urls = {"https://t.me/maybeAbends": "bx bxl-telegram",
        	"https://github.com/Abends2": "bx bxl-github",
        	"https://discordapp.com/users/Abends#5734": "bx bxl-discord-alt"}


# home page
@app.route("/")
@app.route("/home")
def home_page():
	return render_template('home.html', title="Home", menu=header_urls_nav, urls=footer_urls)


# keyboards page
@app.route("/keyboards")
def keyboards_page():
	return render_template('keyboards.html', title="Keyboards", menu=header_urls_nav, urls=footer_urls)


# Login page
@app.route("/login")
def login():
	return render_template('login.html', title="Login")


if __name__ == "__main__":
	app.run(debug=True)