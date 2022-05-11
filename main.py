from flask import Flask, render_template


app = Flask(__name__, static_folder="static_files")


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


if __name__ == "__main__":
	app.run(debug=True)