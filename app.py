from flask.helpers import url_for
from jinja2.utils import urlize
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash 
from flask import Flask, render_template, request, flash     
from flask_admin import Admin
from flask_login import LoginManager, login_user
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "login.html"

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)
    login_manager.init_app(app)
    from models import User
        
    @app.route("/", methods=["GET","POST"])
    def login():
         if request.method == "POST":
                name = request.form["name"]
                password = request.form["password"]
        
                user = User.query.filter_by(name=name).first()
        
                if not user:
                    flash("Credenciais invalidas")
                    return redirect(url_for("login"))    
                if not check_password_hash(user.password, password):
                    flash("Credenciais invalidas")
                    return redirect(url_for("login"))
                
                login_user(user)
                return redirect(urlize("/admin/"))
            
         return render_template("login.html")    
       
    
    import admin as administrator
    admin = Admin(app, name="Intrack",template_mode="bootstrap3")
    administrator.init_app(admin)
    
    return app 