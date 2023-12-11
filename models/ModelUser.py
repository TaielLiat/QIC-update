from .entities.User import User

class ModelUser():
    
    @classmethod
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT id_empleado, username, password, nombre, apellido, is_admin FROM empleados 
                    WHERE username = '{}' """.format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user_id, username, password, nombre, apellido, is_admin = row
                user = User(user_id, username, User.check_password(password, user.password), nombre, apellido, is_admin)
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id_empleado, username, nombre, apellido, is_admin FROM empleados WHERE id_empleado = {}".format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None,row[2], row[3], row[4])
                print ("")
            else:
                return None
        except Exception as ex:
            raise Exception(ex)