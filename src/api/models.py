from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), nullable=False, unique=True)
    _password = db.Column(db.String(256), nullable=False)



    def serialize(self):
        return {
            "email": self.email,
        }
    
    @hybrid_property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,password):
        self._password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self._password,password)