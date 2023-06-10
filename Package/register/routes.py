from flask import render_template,redirect,url_for,Blueprint
from Package.register.forms import RegistrationForm

register = Blueprint('register',__name__)

@register.route('/Thanks')
def Thanks():
    return render_template('Thanks.html',title='Thanks')

@register.route('/register',methods=['GET','POST'])
def register_page():
    form=RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('register.Thanks'))
    return render_template('forms.html',title='Register',form=form)