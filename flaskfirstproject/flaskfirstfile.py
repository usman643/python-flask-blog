from flask import Flask , render_template
app = Flask(__name__)


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
		"content":"second Blog Post",
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




if __name__ == '__main__' :
	app.run(debug=True)

