from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id_empleado, username, password, nombre="", apellido="", is_admin="") -> None:
        self.id_empleado = id_empleado
        self.username = username
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.is_admin = is_admin
        
    def set_admin(self, is_admin):
        self.is_admin = is_admin
        
    def get_id(self):
        return str(self.id_empleado)
    
    @classmethod
    def hash_password(self, password):
        return generate_password_hash(password, method='sha256')
    
    @classmethod
    def check_password(self,hashed_password,password):
        return check_password_hash(hashed_password,password)