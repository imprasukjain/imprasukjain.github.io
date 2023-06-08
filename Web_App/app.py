from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY']='a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0'



@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html',title='Home')

@app.route('/error')
def error():
    return render_template('Error.html',title='Error')

@app.route('/Thanks')
def Thanks():
    return render_template('Thanks.html',title='Thanks')

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('Thanks'))
    return render_template('forms.html',title='Register',form=form)





if __name__ == '__main__':
    app.run(host='localhost',debug=True,port=5000)
