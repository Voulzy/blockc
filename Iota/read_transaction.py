from iota import Iota
from iota import Tag 
import numpy as np
from rsa_signature import *


#####definition des variables a récuperer####
km={}
conso={}
usure={}
response = {}

########### Fin definition variable


### Get signature, encode in base64
def get_signature(message):
	return message.decode().split('?')[2]


## Get Value (150 for example)
def get_value(message):
	return message.decode().split('?')[1]

#### Verify if the signature is OK
def get_verify_IOTA(message,public_key):
	print("Verification signature ...")
	signature=get_signature(message)
	data=message.decode().split('?')[0]+'?'+message.decode().split('?')[1]+'?'
	data=data.encode("utf-8")
	data=SHA256.new(data)
	print(verify(public_key,data,signature))
	print("Signature OK")






def get_dicts(UID):
	print ("Connexion to the iota devnet...")

	api = Iota('https://nodes.devnet.iota.org:443', testnet = True)

	###### A utiliser pour saisi manuel de l'uid

	#input=input("Quel est l'UID de la voiture ?")
	#print("UID saisi : ",input) 

	#####
	pub_jey=import_public_key()
	print( "Get all the transaction from the concessionaire address..")
	address= ['XJWGTWXL9JBKRGXONOXCIFLALYGAHFQKKSPFADNMJLDOZYNDWCPVUWJCK9OYBUNYNWVHQDKOHVDZE9PTD']

	## get all transaction done to the adress
	transactions = api.find_transaction_objects(addresses=address)
	#UID='AA9999999999999999999999999'
	print("Parcours des transaction")
	for transaction in transactions['transactions']:
	  # Ignore input transactions; these have cryptographic signatures,
	  # not human-readable messages.
		if transaction.value < 0:
			continue
		message = transaction.signature_message_fragment
		date = transaction.timestamp
		Tag_t=transaction.tag
		### Only this transaction hash is OK for this example
		
		if message is None:
			print('(None)')
		else :
			if Tag_t==UID :
				code=message.decode().split('?')[0]
				if code=='km' :
					km[transaction.timestamp] = get_value(message)
					get_verify_IOTA(message,pub_jey)
				elif code=='conso' :
					conso[get_value(message)] = transaction.timestamp
				elif code=='usure' :
					usure[get_value(message)] = transaction.timestamp
				else:
					print('Code introuvable')
			else:
				return "error"
	response["km"] = km
	response["conso"] = conso
	response["usure"] = usure
	return response



print('Km : ',km)
print(' Conso : ',conso)
print("Usure : ",usure)
