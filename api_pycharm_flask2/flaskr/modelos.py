from from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_user = db.Column(db.String(128))
    password = db.Column(db.String(128))
    album = db.relationship('Album', backref='user', lazy=True)

    def __repr__(self):
        return "{} - {} - {}".format(self.id, self.nombre_user, self.password)

cancion_album = db.Table('cancion_album',
    db.Column('cancion_id', db.Integer, db.ForeignKey('cancion.id')),
    db.Column('album_id', db.Integer, db.ForeignKey('album.id'))
)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    año = db.Column(db.Integer)
    descripcion = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cancion = db.relationship('Cancion', secondary=cancion_album, back_populates='album')

    def __repr__(self):
        return "{} - {} - {} - {}".format(self.id, self.titulo, self.año, self.descripcion)

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    album = db.relationship('Album', secondary=cancion_album, back_populates='cancion')

    def __repr__(self):
        return "{} - {} - {} - {}".format(self.titulo, self.minutos, self.segundos, self.interprete)

class MedioTipo(Enum):
    DISCO = 'disco'
    CASSETTE = 'cassette'
    CD = 'cd'

class Medio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Enum(MedioTipo))

    def __repr__(self):
        return f"Medio(id={self.id}, tipo={self.tipo})"