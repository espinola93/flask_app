from flask import render_template
from flask import Flask


app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/home_additions')
def gallery():
	return render_template('home_additions.html')
