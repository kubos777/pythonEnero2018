import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
clave = ''
verificacion = ''
bot = Bot(clave)

@app.route("/", methods=('GET','POST'))
def recibir_mensaje():
	if request.method == 'GET': #Si es método get
		codigoValidacion = request.args.get('hub.verify_token')
		return verify_fb_token(codigoValidacion)
	else:#POST
		output = request.get_json()
		for event in output['entry']:
			messaging = event['messaging']
			for message in messaging:
				if message.get('message'):
					#Recibir identificacion de usario
					recipient_id = message['sender']['id']
					if message['message'].get('text'):
						response_sent_text = get_message()
						send_message(recipient_id, response_sent_text)
					if message['message'].get('attachments'):
						response_sent_nontext = get_message()
						send_message(recipient_id, response_sent_nontext)
	return "Mensaje procesado"

def verify_fb_token(codigoValidacion):
	if codigoValidacion == verificacion:
		return request.args.get("hub.challenge")
	return 'Verificación invalida'

#Que va a hacer cuando reciba el mensaje
def get_message():
	respuestas = ["ahorita no joven", "Cuantos más peña?", "Que rollo dijo el pollo", "AMO PROTECO", "XD"]

	return random.choice(respuestas)

def send_message(recipient_id, answer):

	bot.send_text_message(recipient_id,answer)
	return "Exito...."

if __name__ == "__main__":
	app.run()