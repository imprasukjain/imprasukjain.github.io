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
@register.route('/results',methods=['GET','POST'])
def results():
    form = ResultsForm()
    if form.validate_on_submit():
        name = form.name.data
        marks = form.marks.data
        status = "Pass" if marks >= 40 else "Fail"
        return render_template('marks.html', title='Results',form = form, name=name, marks=marks, status=status)
    return render_template('marks.html', title='Results', form=form)
