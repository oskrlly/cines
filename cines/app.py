from flask import Flask , jsonify
from users_registred import users #para importar los archivos creados dentro del proyecto que se usaran
from login import login
from movies import m1
app = Flask(__name__) #ejecutamo flask como servidor 

@app.route('/', methods=['GET']) #indicamos la ruta de incio con el metodo get 
def ping (): #definimos una funcion para dar la bienvenida 
    return jsonify({"response": "Bienvenido"})

@app.route('/users')
def usercine():
    return jsonify({"users": users})

@app.route('/login')
def login_ses():
        return jsonify({"login" : login})

@app.route('/movies')
def moviesfun():
    return jsonify({"movies": m1})

if __name__ == '__main__': # Sejecutar solo si este archivo se esta ejecutando como el archivo principal 
    
    app.run(host="0.0.0.0", port=4000 , debug= True) # colocamos hots 0.0.0.0 ya que segun la documentacion de flask asi podremos acceder desde cualquier direccion, iniciamos la aplicacion  en el puerto 4000 y colocamos debug true ya que asi al realizar cambios le servidor se actualizara automaticamente 

