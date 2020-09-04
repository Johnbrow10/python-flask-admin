from flask_admin.contrib.sqla import ModelView
from flask import redirect
from wtforms.fields import PasswordField
from werkzeug.security import generate_password_hash 
from flask_login import current_user

from models import CursoModel, Instrutor, User
from app import db

class CursoView(ModelView):
    column_editable_list = (
        'instrutor','nome', 'descricao_curta',
        'descricao_longa','url_imagem','url_video_intro',
        'restrito','estrelas','tempo_total','criado_em'
        )
    form_edit_rules = {
        'instrutor','nome', 'descricao_curta',
        'descricao_longa','url_imagem','url_video_intro',
        'restrito','estrelas','tempo_total','criado_em'
        }
    
    column_searchable_list = {'nome'}
    edit_modal = True
    
 
    column_filters = ['nome','instrutor']
    column_list = (
        'instrutor','nome', 'descricao_curta',
        'descricao_longa','url_imagem','url_video_intro',
        'restrito','estrelas','tempo_total','criado_em'
    )
    
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargts):
        return redirect("/")
    
class InstrutorView(ModelView):
    
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargts):
        return redirect("/")
    
class UserView(ModelView):
    column_exclude_list = ('password')
    
    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(form.password.data)
    
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargts):
        return redirect("/")
  
def init_app(admin):
      
    admin.add_view(CursoView(CursoModel,db.session))
    admin.add_view(InstrutorView(Instrutor, db.session))
    admin.add_view(UserView(User, db.session))
    