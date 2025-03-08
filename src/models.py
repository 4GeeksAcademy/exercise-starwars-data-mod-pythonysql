from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import create_engine, String, ForeignKey

db = SQLAlchemy()

class User (db.Model):

    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False,unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[str] = mapped_column(nullable=False)
    personaje = db.relationship('Personaje')
    planet = db.relationship('Planet')
    specie = db.relationship('Specie')
    vehicle = db.relationship('Vehicle')

    def serialize_user(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'date': self.date,
          
        }
 
  
class Personaje (db.Model):
    __tablename__ = 'personaje'
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname_per: Mapped[str] = mapped_column(nullable=False,unique=True)
    descrip_per: Mapped[str] = mapped_column(nullable=False)
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    def serialize_personaje(self):
        return {
            'id': self.id,
            'firstname_per': self.firstname_per,
            'descrip_per': self.descrip_per,
            'user_id': self.meta_keywords,
            
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname_pla: Mapped[str] = mapped_column(nullable=False,unique=True)
    descrip_pla: Mapped[str] = mapped_column(nullable=False)
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    def serialize_planet(self):
         return {
            'id': self.id,
            'firstname_pla': self.firstname_per,
            'descrip_pla': self.descrip_per,
            'user_id': self.meta_keywords,
            
        }

class Specie(db.Model):
    __tablename__ = 'specie'
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname_spe: Mapped[str] = mapped_column(nullable=False,unique=True)
    descrip_spe: Mapped[str] = mapped_column(nullable=False)
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    def serialize_specie(self):
         return {
            'id': self.id,
            'firstname_spe': self.firstname_per,
            'descrip_spe': self.descrip_per,
            'user_id': self.meta_keywords,
            
        }

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname_vehi: Mapped[str] = mapped_column(nullable=False,unique=True)
    descrip_vehi: Mapped[str] = mapped_column(nullable=False)
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    def serialize_vehicle(self):
         return {
            'id': self.id,
            'firstname_vehi': self.firstname_per,
            'descrip_vehi': self.descrip_per,
            'user_id': self.meta_keywords,
            
        }

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
