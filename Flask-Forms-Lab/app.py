from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "Maher"
password = "123"
facebook_friends=["Firas","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods = ["GET", "POST"])  # '/' for the default page
def login():
	if request.method == "POST":
		username2 = request.form["username"]
		password2 = request.form["password"]
		if username2 == username and password2 == password:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

	if request.method == 'GET':
		return render_template('login.html')


@app.route('/home', methods = ["GET", "POST"]) 
def home():
	if request.method == "POST":
		friend = request.form['friend']
		return redirect(url_for('friend_exists'))
	else:
		return render_template('home.html', facebook_friends = facebook_friends)



@app.route('/friend_exists/<string:name>', methods = ["GET", "POST"]) 
def friend_exists(name):
	return render_template('friend_exists.html', facebook_friends = facebook_friends, name = name)





if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)