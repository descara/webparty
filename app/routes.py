from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Reuben'}
	posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
        	'author': {'username': 'Danii'},
        	'body': 'I am quarantined at home, this sucks!'
        }
    ]
	return render_template('index.html', title="Main", user=user, posts=posts)