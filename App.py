
from datetime import datetime, timedelta
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_mysqldb import MySQL
from models.entities.User import User
from models.ModelUser import ModelUser

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Hermosa10111'
app.config['MYSQL_DB'] = 'qicdatabase'
mysql = MySQL(app) #creo conexion
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql, id)
app.secret_key = 'msk'

########## PANTALLA DE INICIO ##########

###########  ############

@app.route('/')#PANTALLA DE INICIO DE LA PAGINA
def Index(): 
    return render_template('login.html')

@app.route('/inicio')#PANTALLA DE INICIO DE LA PAGINA
@login_required
def Inicio(): 
    return render_template('inicio.html')

########## fin PANTALLA DE INICIO ##########

########## PANTALLA DE CLIENTES ########## 

@app.route('/clientes') # PANTALLA DE CLIENTES
def Clientes():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM clientes')
    datos = cursor.fetchall() #traer todos los datos en una variable
    return render_template('cliente.html', clientes = datos)

@app.route('/agregar_cliente', methods=['POST']) # PANTALLA DE ADICIÓN DE CLIENTE
def crearCliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO clientes (nombre, apellido, telefono, email) VALUES(%s, %s, %s, %s)', (nombre, apellido, telefono, email))
        mysql.connection.commit() #ejecuta la consulta
        flash('Cliente agregado correctamente!')
        return redirect(url_for('Clientes'))

@app.route('/editar_cliente/<id>', methods=['POST', 'GET']) # PANTALLA DE EDICIÓN DE CLIENTE
def editarCliente(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM clientes WHERE id_cliente = %s', [id])
    datos = cursor.fetchall()
    return render_template('editar_cliente.html', cliente=datos[0])

@app.route('/modificar_cliente/<id>', methods = ['POST']) # ENVÍO FORMULARIO DE EDICIÓN DE CLIENTE
def modificarClientes(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE clientes
        SET nombre = %s,
            apellido = %s,
            telefono = %s,
            email = %s
        WHERE id_cliente = %s
    """, (nombre, apellido, telefono, email, id))
    mysql.connection.commit()
    flash('Cliente actualizado correctamente!')
    return redirect(url_for('Clientes'))

@app.route('/borrar_cliente/<id>') # ELIMINO CLIENTE
def borrarCliente(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM clientes WHERE id_cliente = %s', id)
    mysql.connection.commit()
    flash('Cliente removido correctamente!')
    return redirect(url_for('Clientes'))

########## fin PANTALLA DE CLIENTES ##########

########## PANTALLA DE EMPLEADOS ########## # SIN ERRORES 

@app.route('/empleados') # PANTALLA DE EMPLEADOS 

def Empleados():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM empleados')
    datos = cursor.fetchall()
    return render_template('empleados.html', empleados = datos)

@app.route('/nuevo_empleado') # PANTALLA DE ADICION DE EMPLEADO
def nuevoEmpleado():
    return render_template('nuevo_empleado.html')

@app.route('/agregar_empleado', methods=['POST']) # ENVIO FORMULACIO DE ADICION DE EMPLEADO
def crearEmpleado():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
        direccion = request.form['direccion']
        cuit = request.form['cuit']
        cuil = request.form['cuil']
        username = request.form['username']
        password = request.form['password']
        is_admin = request.form['is_admin']
        password_hashed = hasheoPassword(password)
        cursor = mysql.connection.cursor()
        cursor.execute('''
        INSERT INTO empleados 
        (nombre, apellido, telefono, email, direccion, 
        cuit, cuil, username, password, is_admin) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
        (nombre, apellido, telefono, email, direccion, cuit, cuil, username, password_hashed, is_admin))
        mysql.connection.commit()
        flash('Empleado agregado correctamente!')
        return redirect(url_for('Empleados'))

@app.route('/editar_empleado/<id>', methods=['POST', 'GET']) # PANTALLA DE EDICION DE EMPLEADO
def editarEmpleado(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM empleados WHERE id_empleado = %s', [id])
    datos = cursor.fetchall()
    return render_template('editar_empleado.html', empleado=datos[0])

@app.route('/modificar_empleado/<id>', methods = ['POST']) # ENVIO FORMULARIO DE EDICION DE EMPLEADO
def modificarEmpleados(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
        direccion = request.form['direccion']
        cuit = request.form['cuit']
        cuil = request.form['cuil']
        username = request.form['username']
        password = request.form['password']
        is_admin = request.form['is_admin']
        cursor = mysql.connection.cursor()
        cursor.execute ("""SELECT password FROM empleados WHERE id_empleado = %s """, id)
        datos = cursor.fetchall()
        if datos[0][0] != password:
            password = hasheoPassword(password)
        cursor.execute("""
        UPDATE empleados
        SET nombre = %s,
            apellido = %s,
            telefono = %s,
            email = %s,
            direccion = %s,
            cuit = %s,
            cuil = %s,
            username = %s,
            password = %s,
            is_admin = %s
        WHERE id_empleado = %s
    """, (nombre, apellido, telefono, email, direccion, cuit, cuil, username, password, is_admin, id))
    mysql.connection.commit()
    flash('Empleado actualizado correctamente!')
    return redirect(url_for('Empleados'))

@app.route('/borrar_empleado/<id>') # ELIMINO EMPLEADO
def borrarEmpleado(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM empleados WHERE id_empleado = %s', id)
    mysql.connection.commit()
    flash('Empleado removido correctamente!')
    return redirect(url_for('Empleados'))

########## fin PANTALLA DE EMPLEADOS ##########

def hasheoPassword(password): #### CONVIERTE LA CONTRASEÑA EN UN CÓDIGO INDESCIFRABLE
    return User.hash_password(password)

########## PANTALLA DE MESAS ########## # CAMBIAR LOS CURSOR.EXECUTE POR FOREIGN KEYS

@app.route('/mesas')#PANTALLA DE MESAS
def Mesas():
    cursor = mysql.connection.cursor()
    cursor.execute ('SELECT * FROM mesas')
    mesas = cursor.fetchall()
    cursor.execute('''SELECT m.id_mesa, m.estado, s.id_servicio, s.id_cliente, c.nombre, s.tamano_grupo, s.senia, s.tipo_servicio, s.hora_inicio
        FROM mesas m
        LEFT JOIN servicios s ON m.id_mesa = s.id_mesa AND s.hora_inicio IS NOT NULL
        LEFT JOIN clientes c ON s.id_cliente = c.id_cliente
                ''')
    servicios = cursor.fetchall()
    #compararFechas()
    return render_template('mesas.html', servicios = servicios, mesas = mesas)

#def compararFechas(): # COMPARA FECHAS PARA DAR AVISOS DE RESERVAS PROXIMAS
    
    cursor.execute("""SELECT servicios.id_servicio, servicios.fecha, servicios.hora_inicio, mesas.estado
                FROM mesas
                RIGHT JOIN servicios
                ON mesas.id_mesa = servicios.id_mesa
                WHERE servicios.tipo_servicio = "reserva" """)
    horarios = cursor.fetchall()
    
@app.route('/agregar_mesa', methods=['POST']) ## SIN PROBLEMAS
def crearMesa():
    if request.method == 'POST':
        id_mesa = request.form['id_mesa']
        estado = request.form['estado']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO mesas (id_mesa, estado) VALUES(%s, %s)', [id_mesa, estado])
        mysql.connection.commit() #ejecuta la consulta
        flash('Mesa agregada correctamente!')
        return redirect(url_for('Mesas'))

@app.route('/borrar_mesa', methods=['POST']) # POP UP ELIMINO MESA 
def borrarMesa():
    if request.method == 'POST':
        id = request.form['id_mesa']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT estado FROM mesas WHERE id_mesa = %s', [id])
        estado = cursor.fetchall() #traer todos los datos en una variable
        str = convertirTupla(estado[0])
        if str == "ocupado":
            flash('Mesa actualmente en uso. Finaliza el servicio antes de eliminarla.')
        else:  
            cursor.execute('DELETE FROM mesas WHERE id_mesa = %s', [id])
            mysql.connection.commit()
            flash('Mesa removida correctamente!')
        return redirect(url_for('Mesas'))
def convertirTupla(palabra):
    str = ''
    for letra in palabra:
        str = str + letra
    return str      
   
@app.route('/cambiar_estado_mesa/', methods = ['POST']) # POP UP CAMBIO ESTADO DE LA MESA
def modificarEstadoMesa():
    if request.method == 'POST':
        id = request.form['id_mesa']
        estado = request.form['estado']
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE mesas
        SET estado = %s
        WHERE id_mesa = %s
    """, (estado, id))
    mysql.connection.commit()
    flash('Estado de mesa modificado correctamente!')
    return redirect(url_for('Mesas'))

@app.route('/nuevo_servicio/<id>', methods=['POST', 'GET']) # PANTALLA DE CREACION DE SERVICIO DE MESA / ASIGNACION DE MESA
def Servicio(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM mesas WHERE id_mesa = %s', [id])
    mesa = cursor.fetchall()
    cursor.execute('SELECT id_cliente, nombre, apellido FROM clientes')
    clientes = cursor.fetchall()
    cursor.execute('SELECT * FROM mesas where estado = "disponible"')
    disponibles = cursor.fetchall()
    return render_template('nuevo_servicio.html', mesa = mesa, clientes = clientes, disponibles = disponibles)

@app.route('/crear_servicio/<id>', methods = ['POST']) # ASIGNO MESA / ENVIO FORMULARIO DE SERVICIO DE MESA
def asignarMesa(id):
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        grupo = request.form['tamano_grupo']
        #Convierte el horario actual en minutos desde las 00:00
        hora_actual = datetime.now().time()
        hora_minutos = hora_actual.hour * 60 + hora_actual.minute
        fecha_actual = datetime.now()
        fecha = fecha_actual.strftime("%Y-%m-%d")
        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO servicios
            SET id_cliente = %s,
                id_mesa = %s,
                tipo_servicio = "mesa",
                tamano_grupo = %s,
                senia = %s,
                hora_inicio = %s,
                fecha = %s
        """, (id_cliente, [id], grupo, '0', hora_minutos, fecha))
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE mesas 
            SET estado = "ocupado"
            WHERE id_mesa = %s
        """, [id])
    mysql.connection.commit()
    flash('Servicio creado correctamente!')
    return redirect(url_for('Mesas'))
    
@app.route('/ver_mesa/<id_mesa>', methods = ['GET']) # PANTALLA DE VISUALIZACION DE DATOS DE SERVICIO DE MESA
def verMesa(id_mesa):
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM mesas WHERE id_mesa = %s', [id_mesa])
        mesa = cursor.fetchall() 
        cursor.execute('SELECT * FROM servicios WHERE id_mesa = %s AND tipo_servicio = "mesa" ', [id_mesa])
        servicio = cursor.fetchall()
        cursor.execute('SELECT * FROM productos WHERE disponible = "si"')
        productos = cursor.fetchall()
        cursor.execute('''SELECT pm.id_mesa_producto, p.nombre AS nombre_producto, pm.cantidad, p.precio
            FROM mesas m
            JOIN productos_mesa pm ON m.id_mesa = pm.id_mesa
            JOIN productos p ON pm.id_producto = p.id_producto
            WHERE m.id_mesa = %s
        ''', [id_mesa])
        consumos = cursor.fetchall()
        return render_template('ver_mesa.html', mesa = mesa[0], servicio = servicio[0], productos = productos, consumos = consumos)
            
@app.route('/editar_mesa/<id>', methods = ['POST', 'GET']) # PANTALLA DE EDICION DE DATOS DE SERVICIO DE MESA
def editarMesa(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM mesas WHERE id_mesa = %s', [id])
    datos = cursor.fetchall() 
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    cursor.execute('SELECT * FROM servicios WHERE id_mesa = %s', [id])
    servicio = cursor.fetchall()
    cursor.execute('SELECT * FROM mesas where estado = "disponible"')
    disponibles = cursor.fetchall()
    return render_template('editar_mesa.html', mesa = datos[0], servicio = servicio[0], clientes = clientes, disponibles = disponibles )

@app.route('/modificar_mesa/<id>', methods = ['POST']) # ENVIO DATOS DE FORMULARIO DE EDICION DE SERVICIO DE MESA
def modificarMesa(id):
    if request.method == 'POST':
        id_mesa = request.form['id_mesa']
        id_cliente = request.form['id_cliente']
        grupo = request.form['tamano_grupo']
        senia = request.form['senia']
        hora_inicio = request.form['hora_inicio']
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE servicios
        SET id_cliente = %s,
            id_mesa = %s,
            tamano_grupo = %s,
            senia = %s,
            hora_inicio = %s
        WHERE id_servicio = %s
    """, (id_cliente, id_mesa, grupo, senia, hora_inicio, id))

    cursor.execute("""
        UPDATE mesas
        SET senia = %s,
            id_cliente = %s
        WHERE id_mesa = %s
    """, (senia, id_cliente, id_mesa))
    
    mysql.connection.commit()
    flash('Servicio actualizado correctamente!')
    return redirect(url_for('Mesas'))

@app.route('/terminar_servicio/<id_mesa>', methods = ['GET','POST']) # TERMINO SERVICIO DE MESA, BORRO DATOS DE SERVICIO Y LOS ENVIO A ARCHIVO
def terminarServicio(id_mesa):
    hora_fin = datetime.now().strftime("%H:%M")
    hora_fin_min = pasarMinutos(hora_fin)
    cursor = mysql.connection.cursor()
    cursor.execute(""" 
        SELECT id_servicio
        FROM servicios
        WHERE id_mesa = %s
        AND tipo_servicio = 'mesa' 
    """, (id_mesa))

    id_servicioR = cursor.fetchone()
    id_servicio = str(id_servicioR)
    characters = "(',')"
    id_servicio = ''.join(x for x in id_servicio if x not in characters)


    #OBTENER, CALCULAR Y ALMACENAR EL TOTAL
    cursor.execute("""
        SELECT pm.id_mesa, p.nombre, pm.cantidad, p.precio
        FROM productos_mesa pm
        JOIN productos p ON pm.id_producto = p.id_producto
        WHERE pm.id_mesa = %s""", (id_mesa,))
    productos_mesa = cursor.fetchall()
    # Calcular el total multiplicando cantidad por precio
    total = sum(producto[2] * producto[3] for producto in productos_mesa)

    cursor.execute(""" 
    UPDATE servicios
        SET hora_fin = %s
        WHERE id_servicio = %s
    """, (hora_fin_min, id_servicio))

    cursor.execute(""" 
    INSERT INTO archivo_servicios (id_servicio, id_cliente, id_mesa, tipo_servicio, tamano_grupo, senia, hora_inicio, hora_fin, fecha, monto_final)
        SELECT id_servicio, id_cliente, id_mesa, tipo_servicio, tamano_grupo, senia, hora_inicio, hora_fin, fecha, %s AS monto_final
        FROM servicios 
        WHERE id_servicio = %s
    """, [total, id_servicio])
    
    cursor.execute("""
        DELETE FROM qicdatabase.servicios WHERE (id_servicio = %s);
    """, [id_servicio])
    cursor.execute("""
        DELETE FROM qicdatabase.productos_mesa WHERE (id_mesa = %s);
    """, [id_mesa])

    cursor.execute(""" 
    UPDATE mesas
        SET estado = 'disponible'
        WHERE id_mesa = %s
    """, [id_mesa])
    mysql.connection.commit()
    flash('Servicio finalizado correctamente!')
    return redirect(url_for('Mesas'))

########## fin PANTALLA DE MESAS ##########

########## PANTALLA DE RESERVAS ##########

@app.route('/reservas') # PANTALLA DE RESERVAS
def Reservas():
    fecha = datetime.now().strftime("%Y-%m-%d")
    cursor = mysql.connection.cursor()
    cursor.execute("""SELECT clientes.nombre, clientes.apellido, servicios.*
                FROM clientes
                RIGHT JOIN servicios
                ON clientes.id_cliente = servicios.id_cliente
                WHERE tipo_servicio = "reserva" 
                """)
    tser = cursor.fetchall()
    cursor.execute("""SELECT clientes.nombre, clientes.apellido, servicios.*
                FROM clientes
                RIGHT JOIN servicios
                ON clientes.id_cliente = servicios.id_cliente
                WHERE tipo_servicio = "reserva" AND fecha =%s
                """, [fecha])
    ser = cursor.fetchall()
    return render_template('reservas.html', todas = tser, servicios = ser)

@app.route('/nueva_reserva') # PANTALLA DE CREACIÓN DE RESERVA
def nuevaReserva():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM servicios')
    res = cursor.fetchall()
    cursor.execute('SELECT * FROM clientes')
    cli = cursor.fetchall()
    cursor.execute("SELECT * FROM mesas WHERE estado = 'disponible' OR estado = 'ocupado'")
    mes = cursor.fetchall() 
    return render_template('nueva_reserva.html', reservas = res, clientes = cli, mesas = mes)

@app.route('/crear_reserva', methods = ['POST']) # ENVÍO FORMULARIO DE CREACIÓN DE RESERVA 
def crearReserva():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        id_mesa = request.form['id_mesa']
        grupo = request.form['tamano_grupo']
        senia = request.form['senia']
        hora_inicio = request.form['hora_inicio']
        hora_inicio_min = pasarMinutos(hora_inicio)
        fecha = request.form['fecha']
        fechareal = datetime.strptime(fecha, '%Y-%m-%d').strftime('%Y-%m-%d')
        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO servicios
            SET id_cliente = %s,
                id_mesa = %s,
                tipo_servicio = "reserva",
                tamano_grupo = %s,
                senia = %s,
                hora_inicio = %s,
                fecha = %s
        """, (id_cliente, id_mesa, grupo, senia, hora_inicio_min, fechareal))    
    mysql.connection.commit()
    flash('Servicio creado correctamente!')
    return redirect(url_for('Reservas'))

def pasarMinutos(hora_inicio):
    horas, minutos = map(int, hora_inicio.split(':'))
    hora_inicio_int = horas * 60 + minutos
    return hora_inicio_int

@app.route('/ver_reserva/<id>', methods = ['GET']) # PANTALLA DE VISUALIZACIÓN DE DATOS DE RESERVA
def verReserva(id):
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM servicios WHERE id_servicio = %s', [id])
        servicio = cursor.fetchall()
        return render_template('ver_reserva.html', servicio = servicio[0])

@app.route('/editar_reserva/<id>', methods = ['POST', 'GET']) # PANTALLA DE EDICIÓN DE RESERVA
def editarReserva(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM servicios WHERE id_servicio = %s', [id])
    datos = cursor.fetchall()
    cursor.execute('SELECT id_mesa FROM mesas')
    mesas = cursor.fetchall()
    cursor.execute('SELECT id_cliente FROM clientes')
    clientes = cursor.fetchall()
    return render_template('editar_reserva.html', servicio = datos[0], clientes = clientes, mesas = mesas )

@app.route('/modificar_reserva/<id>', methods = ['POST']) # ENVIO FORMULARIO DE EDICIÓN DE RESERVA
def modificarReserva(id):
    if request.method == 'POST':
        id_mesa = request.form['id_mesa']
        id_cliente = request.form['id_cliente']
        grupo = request.form['tamano_grupo']
        senia = request.form['senia']
        hora_inicio = request.form['hora_inicio']
        fecha = request.form['fecha']
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE servicios
        SET id_cliente = %s,
            id_mesa = %s,
            tamano_grupo = %s,
            senia = %s,
            hora_inicio = %s,
            fecha = %s
        WHERE id_servicio = %s
    """, (id_cliente, id_mesa, grupo, senia, hora_inicio, fecha, id))
    mysql.connection.commit()
    flash('Reserva actualizada correctamente!')
    return redirect(url_for('Reservas'))

@app.route('/borrar_reserva/<id>', methods=['GET','POST']) # ELIMINO RESERVA
def borrarReserva(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM servicios WHERE id_servicio = %s', [id])
    mysql.connection.commit()
    flash('Reserva removida correctamente!')
    return redirect(url_for('Reservas'))

@app.route('/iniciar_reserva/<id_servicio>', methods=['GET','POST']) # VERIFICO ESTADO DE MESA EN MODULO MESAS Y ACTUALIZO EL SERVICIO DE RESERVA A MESA
def iniciarReserva(id_servicio):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id_mesa FROM servicios WHERE id_servicio = %s', [id_servicio])
    id_mesa = cursor.fetchone()
    cursor.execute('SELECT estado FROM mesas WHERE id_mesa = %s', [id_mesa])
    estado = cursor.fetchone()
    cursor.execute('SELECT senia, id_cliente FROM servicios WHERE id_servicio = %s', [id_servicio])
    datos = cursor.fetchall()
    characters = "(','`)"
    id_mesa=str(id_mesa)
    id_mesa= ''.join(x for x in id_mesa if x not in characters)
    estado = ''.join(x for x in estado if x not in characters)
    if (estado == "ocupado"):
        flash("Debe desocupar la mesa de la reserva antes de poder iniciar el servicio")
    elif(estado =="no disponible"):
        flash("La mesa seleccionada no se encuentra disponible actualmente. Seleccionar otra.")
    elif(estado =="disponible"):
        cursor = mysql.connection.cursor()

        cursor.execute("""
            UPDATE servicios
            SET tipo_servicio = "mesa"
            WHERE id_servicio = %s
            """, [id_servicio])

        cursor.execute("""
        UPDATE mesas
        SET estado = "ocupado"
        WHERE id_mesa = %s
        """, (id_mesa))
        mysql.connection.commit()
        flash('Reserva iniciada correctamente!')
    return redirect(url_for('Reservas'))

########## fin PANTALLA DE RESERVAS ##########

########## PANTALLA DE MENÚ ##############

@app.route('/menu') # PANTALLA DE EMPLEADOS
def Productos():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM productos')
    datos = cursor.fetchall()
    return render_template('menu.html', productos = datos)

@app.route('/nuevo_producto') # PANTALLA DE ADICION DE PRODUCTO
def nuevoProducto():
    return render_template('nuevo_producto.html')

@app.route('/agregar_producto', methods=['POST']) # ENVIO FORMULACIO DE ADICION DE EMPLEADO
def crearProducto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        disponible = request.form['disponible']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO productos (nombre, precio, disponible) VALUES(%s, %s, %s)', (nombre, precio, disponible))
        mysql.connection.commit()
        flash('Producto agregado correctamente!')
        

############### PANTALLA VER MESA, MENU ######################
@app.route('/agregar_consumo', methods=['POST'])
def agregarConsumo():
    if request.method == 'POST':
        nombre_producto = request.form['nombre_producto']
        id_mesa = request.form['id_mesa']
        cantidad = request.form['cantidad']
    
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT id_producto FROM productos 
            WHERE nombre = %s''', [nombre_producto])
        id_producto = cursor.fetchall()
        cursor.execute("""
            INSERT INTO productos_mesa (id_producto, id_mesa, cantidad)
            VALUES (%s, %s, %s)
        """, (id_producto[0][0], id_mesa, cantidad))
        mysql.connection.commit()
        flash('Consumo agregado correctamente!')
        return redirect(url_for('verMesa', id_mesa=id_mesa))

@app.route('/modificar_consumo', methods=['POST', 'GET']) # PANTALLA DE EDICION DE PRODUCTO
def modificarConsumos():
        if request.method == 'POST':
            id_mesa = request.form['id_mesa']
            nombre = request.form['nombre']
            cantidad = request.form['cantidad']
            cursor = mysql.connection.cursor()

            cursor.execute(''' SELECT id_producto FROM productos 
                WHERE nombre = %s''', [nombre])
            id_producto = cursor.fetchone()

            cursor.execute("""
                UPDATE productos_mesa 
                SET cantidad = %s
                WHERE id_mesa = %s AND id_producto = %s
            """, (cantidad, id_mesa, id_producto))
            mysql.connection.commit()
            flash('Consumo modificado correctamente!')
            return redirect(url_for('verMesa', id_mesa=id_mesa))

@app.route('/borrar_consumo/<id>') 
def borrarConsumo(id):
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id_mesa FROM productos_mesa WHERE id_mesa_producto = %s', [id])
        id_mesa = cursor.fetchone()
        cursor.execute('DELETE FROM productos_mesa WHERE id_mesa_producto = %s', [id])
        mysql.connection.commit()
        flash('Consumo removido correctamente!')
        return redirect(url_for('verMesa', id_mesa=id_mesa[0]))

##################################################################

@app.route('/editar_producto/<id>', methods=['POST', 'GET']) # PANTALLA DE EDICION DE PRODUCTO
def editarProducto(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM productos WHERE id_producto = %s', [id])
    datos = cursor.fetchall()
    return render_template('editar_producto.html', producto=datos[0])

@app.route('/modificar_producto/<id>', methods = ['POST']) # ENVIO FORMULARIO DE EDICION DE PRODUCTO
def modificarProducto(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        disponible = request.form['disponible']
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE productos
            SET nombre = %s,
                precio = %s,
                disponible = %s
            WHERE id_producto = %s
        """, (nombre, precio, disponible, id))
        mysql.connection.commit()
        flash('Producto actualizado correctamente!')
        return redirect(url_for('Productos'))

@app.route('/borrar_producto/<id>') # ELIMINO PRODUCTO
def borrarProducto(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM productos WHERE id_producto = %s', id)
    mysql.connection.commit()
    flash('Producto removido correctamente!')
    return redirect(url_for('Productos'))

########## fin PANTALLA DE MENÚ ##########

########## PANTALLA DE ARCHIVOS ##########

@app.route('/archivos') #PANTALLA DE ARCHIVOS
@login_required
def Archivos():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM archivo_servicios ORDER BY fecha DESC, hora_fin DESC')
    datos = cursor.fetchall()
    print(datos) 
    return render_template('archivos.html', servicios = datos)

########## fin PANTALLA DE ARCHIVOS ##########

########## PANTALLA INICIO DE SESION ##########

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['usuario'], request.form['contrasenia'])
        logged_user=ModelUser.login(mysql,user)
        print (logged_user)
        print(f"ID: {logged_user.id_empleado}")
        print(f"Username: {logged_user.username}")
        print(f"Password: {logged_user.password}")
        print(f"Is Admin: {logged_user.is_admin}")
        if logged_user and logged_user.password:          
            login_user(logged_user)
            return redirect(url_for('Inicio'))
        else:
            flash("Usuario o contraseña incorrecto")
            return render_template('login.html')
    else:
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
    
@app.route('/logged')
@login_required
def logged():
    return render_template('logged.html')

########## fin de PANTALLA DE INICIO DE SESIÓN ##########

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 3000, debug = False)

