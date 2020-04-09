from flask import Flask , render_template , url_for, flash , redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '3c983e8373f6b977c97e67982f421314'

posts=[
	{
		"author":"Muhammad Usman",
		"title":"Blog post 1",
		"content":"First Blog Post",
		"date_posted":"April 21, 2018"
	},
	{
		"author":"Muhammad Usman",
		"title":"Blog post 2",
		"content":"Second Blog Post",
		"date_posted":"April 21, 2017"
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('Home.html', posts=posts)


@app.route("/about")
def about():
	return render_template('about.html', title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account Created for { form.username.data }!' , 'success')
		return redirect(url_for('home'))


	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'a@a.com' and form.password.data == 'password':
			flash(f'You have loggedIn!', 'success')
			return redirect(url_for('home'))
		else:
			flash(f'Something went wrong! Please check email and password', 'danger')
	return render_template('login.html', title='Login', form=form)



if __name__ == '__main__' :
	app.run(debug=True)

