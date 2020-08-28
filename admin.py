from flask_admin.contrib.sqla import ModelView
from flask import redirect
from wtforms.fields import PasswordField
from werkzeug.security import generate_password_hash 
from flask_login import current_user
import uuid

from models import CursoModel
from app import db

class CursoView(ModelView):
    column_editable_list = (
        'instrutor_id', 'nome', 'descricao_curta',
        'descricao_longa','url_imagem','url_video_intro',
        'restrito','estrelas','tempo_total','criado_em'
        )
    form_edit_rules = {
        'instrutor_id', 'nome', 'descricao_curta',
        'descricao_longa','url_imagem','url_video_intro',
        'restrito','estrelas','tempo_total','criado_em'
        }
    
    column_searchable_list = {'nome'}
    edit_modal = True
    
 
    column_filters = ['nome','instrutor_id']
    column_list = [
        'instrutor_id', 'nome', 'descricao_curta',
        'descricao_longa','url_imagem','url_video_intro',
        'restrito','estrelas','tempo_total','criado_em'
    ]
    
 
    # def on_change(self,is_created):
    #     if is_created:
    #         self.curso_id = str(uuid.uuid4())
    #         db.session.add(self)
    #         db.session.commit()

def init_app(admin):
    
    admin.add_view(CursoView(CursoModel,db.session),)
    # admin.add_view(ModelView(Task, db.session))