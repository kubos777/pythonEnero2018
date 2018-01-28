#####################
# Flask con mysql
#####################

#pip install flask
#pip install flask-mysql

from flask import Flask,render_template,json,request
#Flask: es el framework
#render_template: nos va a ayudar a cargar los documentos de HTML5
#json: nos va a permitir hacer uso de objetos tipo JSON
#request: Me va a permitir realizar peticiones por medio de 'GET' Y 'POST'
from flask.ext.mysql import MySQL 
#MysQL me permite conectarme a la base de datos de mysql
from werkzeug import generate_password_hash,check_password_hash

#werkzeug nos permite agregar seguridad a los datos de nuestra base

#Creamos un objeto de tipo MySQL
mysql= MySQL()

#Creamos una app de flask de la siguiente forma
app= Flask(__name__)

#Configuraciones para la conexión
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='deseos'
#127.0.0.1:5000 por default
app.config['MYSQL_DATABASE_HOST']='localhost'

mysql.init_app(app)

#Definimos la ruta básica '/' y su correspondiente manejador
@app.route("/")
#Manejador
def main():
	#return "Sí sirve esta cosa!"  
	return render_template("index.html")

@app.route("/showSignUp")
def showSignUp():
	return render_template("signup.html")

@app.route("/signUp",methods=['POST','GET'])
def signUp():
	#Aquí va el código para la creación de usuarios
	#por medio del metodo POST
	try:
		#Del formulario, obtenemos por medio del id lo que este
		#escrito ahí.
		_name=request.form['inputName']
		_email=request.form['inputEmail']
		_password=request.form['inputPassword']

		#Vamos a revisar si los datos son válidos o estan completos
		#Si es verdad o True significa que los campos estan llenos
		#Si es falso significa que los campos estan vacíos
		if _name and _email and _password:
			#Como ya tenemos la conexión a la base,creamos la conexión
			conn=mysql.connect()
			#Además creamos nuestro cursor
			cursor=conn.cursor()
			#Aquí vamos a encriptar nuestra contraseña
			_hashed_password= generate_password_hash(_password)
			#Llamamos al procedimiento
			cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
			#Guarda los registros que esten en la base
			data=cursor.fetchall()
			#Si ya estan listos los datos
			if len(data) is 0:
				conn.commit()
				return json.dumps({'message':'Usuario creado exitosamente!'})
			else:
				return json.dumps({'error':str(data[0])})
		else:
			return json.dumps({"html":'<span>Te faltan campos por llenar!</span>'})
	except Exception as e:
		return json.dumps({"error":str(e)})
	finally:
		cursor.close()
		conn.close()		



if __name__=='__main__':
	app.run(port=5002)

#Verificamos que funcione en: 127.0.0.1:5002