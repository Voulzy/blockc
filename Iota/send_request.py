from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from rsa_signature import *



def import_file(file):
	with open(file,mode='rb') as file_r:
        	content=file_r.read()
        	return content



def sign_message(message,private_key):
	signature_base_64=sign(private_key,SHA256.new(message))
	print(signature_base_64)
	return TryteString.from_bytes(signature_base_64)

def cast_message(value,private_key):
	###data for hash function
	data=(value).encode("utf-8")
	##message to store in the tangle
	message=TryteString.from_unicode(value)
	signature=sign_message(data,private_key)
	end=TryteString.from_unicode('?')
	message=message+signature+end
	return message


def send_request(value,address,private_key,api,UID):
	message=cast_message(value,private_key)
	tx = ProposedTransaction(
	address=Address(address),
	value = 10,
	tag=Tag(UID),
	message=message
	)

	result = api.send_transfer(transfers=[tx] )
	print('Bundle: ')
	print(result['bundle'].tail_transaction.hash)



if __name__ == "__main__":
	UID=input("Quel est votre tag de voiture ?") 
	private_key=import_private_key('keys/private_concess_request.pem')
	seed=import_file('seed_adress/seed_concessionaire_request.txt')
	api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)
	address=import_file(f'seed_adress/address_car_{UID}.txt')
	send_request('conso?',address,private_key,api,UID)

