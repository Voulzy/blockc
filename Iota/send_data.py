from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from rsa_signature import *
#privatekey of a car, should be remove later


def import_file(file):
	with open(file,mode='rb') as file_r:
        	content=file_r.read()
        	return content



if __name__ == "__main__":


	input_data=input("Quel est votre data a envoyé ?")
	UID=input("Quel est votre tag de voiture ?") 

	#connexion to the devnet, from the seed 
	
	private_key=import_private_key(f'keys/car_{UID}_priv.pem')
	seed=import_file(f'seed_adress/seed_car_{UID}.txt')
	api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)
	address='B9UCJQA9AUNWWQCFKPHYPBXFCSZPKMQI9TWFN9G9BJTHBHZQDXFXTGTPICXFTYKGJKJR9TWLVMVZEVPJX'
	data=input_data.encode("utf-8")
	signature=sign(private_key,SHA256.new(data))
	print(signature)
	signature_trytes=TryteString.from_bytes(signature)
	message=TryteString.from_unicode(input_data)
	end=TryteString.from_unicode('?')
	message=message+signature_trytes+end
	tx = ProposedTransaction(
	address=Address(address),
	value = 10,
	tag=Tag(UID),
	message=message
	) 
	result = api.send_transfer(transfers=[tx] )
	print('Bundle: ')
	print(result['bundle'].tail_transaction.hash)
