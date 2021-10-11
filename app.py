from flask import render_template
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired
from flask_mail import Mail, Message


app = Flask(__name__)
mail= Mail(app)
app.config['SECRET_KEY'] = "development key"

#mail configurations
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'olvera93.eo@gmail.com'
app.config['MAIL_PASSWORD'] = 'Osolemio12'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

#Form class
class ContactForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired(message="Please enter your name")])
	email = StringField("Email",validators=[DataRequired()])
	message = TextAreaField("Message",validators=[DataRequired()])
	
	submit = SubmitField("submit") 

@app.route('/', methods=['GET','POST'])
def index():
	#contact form 
	name = None
	email = None
	message = None
	form = ContactForm()
	#validating form
	if form.validate_on_submit():
		name =form.name.data
		form.name.data = ''
		email =form.email.data
		form.email.data = ''
		message =form.message.data
		form.message.data = ''
		#send email
		msg = Message('espinolasremodeling.com', sender = 'yourId@gmail.com', recipients = ['olvera93.eo@gmail.com'])
		msg.body = "Message: " + "" + message + "\n" + "From: "+ name + "\n" + "Email: " + email
		mail.send(msg)
		return render_template('message_sent.html')
		#send email end
	#contact form end
	return render_template('index.html', name = name, email = email, message=message, form = form)
@app.route('/kitchen_remodeling')
def kitchen_remodeling():
	return render_template('kitchen_remodeling.html')
@app.route('/bathroom_remodeling')
def bathroom_remodeling():
	return render_template('bathroom_remodeling.html')
@app.route('/flooring')
def flooring():
	return render_template('flooring.html')
@app.route('/roofing')
def roofing():
	return render_template('roofing.html')
@app.route('/home_additions')
def home_additions():
	return render_template('home_additions.html')
@app.route('/painting')
def painting():
	return render_template('painting.html')
@app.route('/message_sent')
def message_sent():
	return render_template('message_sent.html')
if __name__ == '__main__':
   app.run(debug = True)
