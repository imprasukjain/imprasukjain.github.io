from flask import Flask,Blueprint


app = Flask(__name__)
app.config['SECRET_KEY']='a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0'

from Package.main.routes import main
from Package.register.routes import register

app.register_blueprint(main)
app.register_blueprint(register)