from iota import Iota
from iota import Tag 
from iota import ProposedTransaction
from iota import Address
from iota import TryteString
import numpy as np
from rsa_signature import *
from datetime import datetime
import time


def get_signature(message):
	return message.decode().split('?')[1]

def import_file(file):
	with open(file,mode='rb') as file_r:
        	content=file_r.read()
        	return content


#### Verify if the signature is OK
def get_verify_IOTA(message,public_key):
	err=1
	print("Verification signature ...")
	signature=get_signature(message)
	data=message.decode().split('?')[0]+'?'
	print("Valeur demander : "+data)
	data=data.encode("utf-8")
	data=SHA256.new(data)
	try : 
		verify(public_key,data,signature)
		print("Signature OK")
	except : 
		err= 0
	finally:
		return err

def sign_message(message,private_key):
	signature_base_64=sign(private_key,SHA256.new(message))
	return TryteString.from_bytes(signature_base_64)

def cast_message(value,private_key):
	###data for hash function
	data=value.encode("utf-8")
	##message to store in the tangle
	message=TryteString.from_unicode(value)
	signature=sign_message(data,private_key)
	end=TryteString.from_unicode('?')
	message=message+signature+end
	return message


def send_transaction(value,address,private_key,api,UID):
	print("Envoie des reponse ...")
	message=cast_message(value,private_key)
	tx = ProposedTransaction(
	address=Address(address),
	value = 10,
	tag=Tag(UID),
	message=message
	)

	result = api.send_transfer(transfers=[tx] )
	




def read_transaction(address,api,UID,publickey):
	print("We search for all the transactions that are ever been made to the car ...")
	transactions = api.find_transaction_objects(addresses=address)
	## We store all the request that are ever been made to our car
	request={}
	for transaction in transactions['transactions']:
		if transaction.value < 0:
			continue
		if transaction.value==0:
			continue

		message = transaction.signature_message_fragment
		date = transaction.timestamp
		print(date)
		Tag_t=transaction.tag

		
		if message is None:
			print('(None)')
		else :
			if Tag_t[0:2]==UID :
				if(get_verify_IOTA(message,publickey)):
					request[date]=message.decode().split('?')[0]
				else:
					print("Bad signature")
	return request


def get_legitimate_request(request,duration):
	print("We select only those made before 24 hours")
	legitimate=[]
	for i in result :
		date=datetime.fromtimestamp(i)
		current_date=datetime.fromtimestamp(time.time())
		delta=current_date-date
		if delta.seconds<duration : 
			legitimate.append(result[i])
	return legitimate

if __name__ == "__main__":
	
	
	public_key=import_public_key('keys/public_concess_request.pem')
	api = Iota('https://nodes.devnet.iota.org:443', testnet = True)
	UID=input("Quel est l'UID de la voiture [AA] [BB] [CC] [DD] ?")
	
	seed=import_file(f'seed_adress/seed_car_{UID}.txt')
	address=[import_file(f'seed_adress/address_car_{UID}.txt')]
	address_concess = 'B9UCJQA9AUNWWQCFKPHYPBXFCSZPKMQI9TWFN9G9BJTHBHZQDXFXTGTPICXFTYKGJKJR9TWLVMVZEVPJX'
	### We get all the request
	result=read_transaction(address,api,UID,public_key)
	##we only keep the legitimate request, and we remove double
	legitimate=list(set(get_legitimate_request(result,50000)))
	privatekey=import_private_key(f'keys/car_{UID}_priv.pem')

	api_respond=Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)
	for i in legitimate : 
		message=i+'?'+"10"+'?'
		send_transaction(message,address_concess,privatekey,api_respond,UID)

		
	