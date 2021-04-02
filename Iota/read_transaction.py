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
	len_1=len(message.decode().split('?'))
	print("Longeur :", len_1)
	signature=message.decode().split('?')[2]
	#for i in range(3,len_1-1):
	#	signature+='?'+message.decode().split('?')[i]
#		print(signature)
#		print("Index : ",i)
	#signature+=message.decode().split('?')[len1-1]
	return signature

## Get Value (150 for example)
def get_value(message):
	return message.decode().split('?')[1]

#### Verify if the signature is OK
def get_verify_IOTA(message,public_key):
	signature=get_signature(message)
	print(signature)
	data=message.decode().split('?')[0]+'?'+message.decode().split('?')[1]+'?'
	print(data)
	data=data.encode("utf-8")
	data=SHA256.new(data)
	print(verify(public_key,data,signature))






def get_dicts(UID):
	print ("Connexion to the iota devnet...")

	api = Iota('https://nodes.devnet.iota.org:443', testnet = True)

	###### A utiliser pour saisi manuel de l'uid

	#input=input("Quel est l'UID de la voiture ?")
	#print("UID saisi : ",input) 

	#####
	pub_jey=import_public_key()
	print( "Get all the transaction from the concessionaire address..")
	address= ['NMSGHUHKOFCJSPCKBBDGQDJPRPWTGT9YCXDVBMUXTGSQAIZLAHSVNNOHEDQRXANVMLS9PWKPJVLCYYBNXYITYTJKJD']

	## get all transaction done to the adress
	transactions = api.find_transaction_objects(addresses=address)
	#UID='AA9999999999999999999999999'
	print("Parcours des transaction")
	for transaction in transactions['transactions']:
	  # Ignore input transactions; these have cryptographic signatures,
	  # not human-readable messages.
		if transaction.value < 0:
			continue

		print(f'Hash : {transaction.hash}:')
		message = transaction.signature_message_fragment
		date = transaction.timestamp
		print(date)
		Tag_t=transaction.tag
		### Only this transaction hash is OK for this example
		if(transaction.hash!='WHFVZWXIT9WCYOV9ZUYSHTFJIVPFFJCYKHZSGG9HCWQHJYPONVGPGHNHCIGMVMVE9F9JIHJBAXYEZX999'):
			continue
		if message is None:
			print('(None)')
		else :
			if Tag_t==UID :
				code=message.decode().split('?')[0]
				if code=='km' :
					km[get_value(message)] = transaction.timestamp
					#get_verify_IOTA(message,pub_jey)
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
