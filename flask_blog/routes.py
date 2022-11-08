from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post

#def test_connection(self):
 #   with app.app_context():
        #test code



posts = [
	{
		'author': "John Doe",
		'title': "ABc",
		'comment': "First post comment",
		'date_posted': 'Nov 1, 2022'
	},

	{
		'author': "Jane Doe",
		'title': "123",
		'comment': "Second post comment",
		'date_posted': "Nov 2, 2022"
	},

	{
		'author': "Janise Doe",
		'title': "Abc123",
		'comment': "Third post comment",
		'date_posted': "Nov 3, 2022"
	}
]

@app.route("/")


@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', posts='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		# "f-string" for passing a variable
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST']) ##### TypeError: The view function for 'login' did not return a valid response. 
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return render_template('login.html', title='Login', form=form)

