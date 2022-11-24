from flask import Flask , jsonify, render_template, request
from flask_mysqldb import MySQLdb
from users_registred import users #para importar los archivos creados dentro del proyecto que se usaran
from login import login
from movies import m1

app = Flask(__name__) #ejecutamo flask como servidor 

dbase = MySQLdb.connect(
    host ="localhost",
    user ="root",
    passwd  ="",
    db ="cines")

@app.route('/', methods=['GET']) #indicamos la ruta de incio con el metodo get 
def ping (): #definimos una funcion para dar la bienvenida 
    return render_template('index.html')

@app.route('/users')
def usercine():
    return jsonify({"users": users})

@app.route('/login')
def login_ses():
        return jsonify({"login" : login})

@app.route('/movies', methods=['POST'])
def moviesfun():
    if request.method == 'POST':
        titulo = request.form['titulo']
        url = request.form['url']
        clasificacion = request.form['clasificacion']
        funciones = request.form['funciones']
        id_funciones = request.form['id_funciones']
        fecha_hora = request.form['fecha_hora']
        cur = MySQLdb.Connection()
        cur.cursor = ('INSTER INTO movies ( titulo, url, clasificacion, funciones, id_funciones, fecha_hora) VALUES (%s, %s, %s, %s, %s, %s, %s)', 
        (titulo, url, clasificacion, funciones, id_funciones, fecha_hora))
        MySQLdb.Connection.commit()
        
    return 'recibido'

if __name__ == '__main__': # Sejecutar solo si este archivo se esta ejecutando como el archivo principal 
    
    app.run(host="0.0.0.0", port=4000 , debug= True) # colocamos hots 0.0.0.0 ya que segun la documentacion de flask asi podremos acceder desde cualquier direccion, iniciamos la aplicacion  en el puerto 4000 y colocamos debug true ya que asi al realizar cambios le servidor se actualizara automaticamente 

