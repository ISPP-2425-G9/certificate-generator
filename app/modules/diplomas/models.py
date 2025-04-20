import re
from datetime import datetime
from sqlalchemy.orm import validates
import pandas as pd
from app import db
import random
import string


class Diploma(db.Model):
    __tablename__ = "diploma"

    id = db.Column(db.Integer, primary_key=True)
    apellidos = db.Column(db.String(120), nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    file_path = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    sent = db.Column(db.Boolean, default=False, nullable=False, server_default="0")

    @validates('correo')
    def validate_correo(self, key, correo):
        print(f"Validando correo: {correo}")
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", correo):
            raise ValueError("Correo no tiene un formato válido.")
        return correo
    

    @classmethod
    def from_excel_row(cls, row):        
        def generate_file_path(correo):
            random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            return f"docs/diplomas/{correo}_{random_str}.pdf"

        return cls(
            apellidos=row["Apellidos"],
            nombre=row["Nombre"],
            correo=row["Correo"],
            file_path=generate_file_path(row["Apellidos"])
        )
        
        
        
class DiplomaTemplate(db.Model):
    __tablename__ = 'diploma_templates'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), unique=True, nullable=False)
    custom_text = db.Column(db.String(500), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
    

