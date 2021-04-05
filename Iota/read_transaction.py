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

#### Verify if the signature is OK. If ok, return 1, if not return 0
def get_verify_IOTA(message,public_key):
	err=1
	print("Verification signature ...")
	signature=get_signature(message)
	data=message.decode().split('?')[0]+'?'+message.decode().split('?')[1]+'?'
	data=data.encode("utf-8")
	data=SHA256.new(data)
	try : 
		verify(public_key,data,signature)
		print("Signature OK")
	except : 
		err= 0
	finally:
		return err



def import_file(file):
	with open(file,mode='rb') as file_r:
        	content=file_r.read()
        	return content



def get_dicts(UID):
	print ("Connexion to the iota devnet...")
	##for the return 
	find=0
	api = Iota('https://nodes.devnet.iota.org:443', testnet = True)

	#Import public key for authentification
	pub_jey=import_public_key(f'keys/car_{UID}_pub.pem')

	print( "Get all the transaction from the concessionaire address..")
	test=import_file('seed_adress/address_concess_store.txt')
	print(test)
	address= [test]

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

		
		if message is None:
			print('(None)')
		else :
			if Tag_t[0:2]==UID :
				code=message.decode().split('?')[0]
				if code=='km' :
					km[transaction.timestamp] = get_value(message)
					find = get_verify_IOTA(message,pub_jey)
				elif code=='conso' :
					conso[transaction.timestamp] = get_value(message)
					find = get_verify_IOTA(message,pub_jey)
				elif code=='usure' :
					usure[transaction.timestamp] = get_value(message)
					find = get_verify_IOTA(message,pub_jey)
				else:
					print('Code introuvable')
	if find == 0 :
		return "error"
	response["km"] = dict(sorted(km.items()))
	response["conso"] = dict(sorted(conso.items()))
	response["usure"] = dict(sorted(usure.items()))
	return response



print('Km : ',km)
print(' Conso : ',conso)
print("Usure : ",usure)
