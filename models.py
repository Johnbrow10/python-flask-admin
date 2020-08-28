from app import db
import uuid


def generate_uuid():
    return str(uuid.uuid4())

class CursoModel(db.Model):
    __tablename__ = 'Curso'

    curso_id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    instrutor_id = db.Column(db.String(30))
    nome = db.Column(db.String(80))
    descricao_curta = db.Column(db.String(400))
    descricao_longa = db.Column(db.Text)
    url_imagem = db.Column(db.String(80))
    url_video_intro = db.Column(db.String(80))
    restrito = db.Column(db.String(1))
    estrelas = db.Column(db.Float(precision=1))
    tempo_total = db.Column(db.Integer)
    criado_em = db.Column(db.String(20))


    def __init__(self, curso_id,instrutor_id, nome, descricao_curta, descricao_longa, url_imagem, url_video_intro, 
    restrito, estrelas, tempo_total, criado_em):
        self.curso_id = curso_id
        self.instrutor_id = instrutor_id
        self.nome = nome
        self.descricao_curta = descricao_curta
        self.descricao_longa = descricao_longa
        self.url_imagem = url_imagem
        self.url_video_intro = url_video_intro
        self.restrito = restrito
        self.estrelas = estrelas
        self.tempo_total = tempo_total
        self.criado_em = criado_em

    def json(self):
        return {
            'curso_id': self.curso_id,
            'instrutor_id': self.instrutor_id,
            'nome': self.nome,
            'descricao_curta': self.descricao_curta,
            'descricao_longa': self.descricao_longa,
            'url_imagem': self.url_imagem,
            'url_video_intro': self.url_video_intro,
            'restrito': self.restrito,
            'estrelas': self.estrelas,
            'tempo_total': self.tempo_total,
            'criado_em': self.criado_em
        }
        

    @classmethod
    def find_curso(cls, curso_id):
        curso = cls.query.filter_by(curso_id=curso_id).first()
        if curso:
            return curso
        return None

    # def save_curso(self):
    #     self.curso_id = str(uuid.uuid1())
    #     db.session.add(self)
    #     db.session.commit()

    def update_curso(self, instrutor_id, nome, descricao_curta, descricao_longa, url_imagem, url_video_intro, restrito, 
    estrelas, tempo_total, criado_em):
        self.instrutor_id = instrutor_id
        self.nome = nome
        self.descricao_curta = descricao_curta
        self.descricao_longa = descricao_longa
        self.url_imagem = url_imagem
        self.url_video_intro = url_video_intro
        self.restrito = restrito
        self.estrelas = estrelas
        self.tempo_total = tempo_total
        self.criado_em = criado_em

    def delete_curso(self):
        db.session.delete(self)
        db.session.commit()





# def current_user(user_id):
#     return User.query.get(user_id)

# class User(db.Model):  
#     __tablename__ = 'users'
    
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(85),nullable=True)
#     email = db.Column(db.String(85), nullable=True,unique=True, index=True )
#     password = db.Column(db.String(255), nullable=True)
#     tasks = db.relationship('Task', backref='user')
#     profile = db.relationship('Profile', backref='user')
    
    
#     def __repr__(self):
#         return self.name
    
# class Profile(db.Model): 
#     __tablename__ = 'profiles'
    
#     id = db.Column(db.Integer, primary_key=True)
#     cpf = db.Column(db.String(20), nullable=False,unique=True, index=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
#     def __repr__(self):
#         return self.cpf
    

# class Task(db.Model): 
#     __tablename__ = 'tasks'
    
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(85),nullable=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
#     def __repr__(self):
#         return self.name
    