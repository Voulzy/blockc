from iota import Iota
from iota import Tag 
import numpy as np
from rsa_signature import *
from datetime import datetime
import time


def get_signature(message):
	return message.decode().split('?')[1]


#### Verify if the signature is OK
def get_verify_IOTA(message,public_key):
	print("Verification signature ...")
	signature=get_signature(message)
	data=message.decode().split('?')[0]+'?'
	data=data.encode("utf-8")
	data=SHA256.new(data)
	print(verify(public_key,data,signature))
	print("Signature OK")
	return 1

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


def send_request(value,address,private_key):
	message=cast_message(value,private_key)
	tx = ProposedTransaction(
	address=Address(address),
	value = 10,
	tag=Tag(b'AA'),
	message=message
	)

	result = api.send_transfer(transfers=[tx] )
	print('Bundle: ')
	print(result['bundle'].tail_transaction.hash)




def read_transaction(address,api,UID,publickey):
	transactions = api.find_transaction_objects(addresses=address)
	## We store all the request that are ever been made to our car
	request={}
	for transaction in transactions['transactions']:
		if transaction.value < 0:
			continue

		message = transaction.signature_message_fragment
		date = transaction.timestamp
		print(date)
		Tag_t=transaction.tag

		
		if message is None:
			print('(None)')
		else :
			if Tag_t[0:2]==UID :
				get_verify_IOTA(message,publickey)
				request[date]=message.decode().split('?')[0]
	return request


def get_legitimate_request(request):
	legitimate=[]
	for i in result :
		date=datetime.fromtimestamp(i)
		current_date=datetime.fromtimestamp(time.time())
		delta=current_date-date
		if delta.seconds<50000 : 
			legitimate.append(result[i])
	return legitimate

if __name__ == "__main__":
	file="../python/publickey.pem"
	public_key=import_public_key(file)
	api = Iota('https://nodes.devnet.iota.org:443', testnet = True)
	address=['MRHDWPXVP9RVDBXNJRMJQQEREZTPAEUUDBPCBFQBLRUMQQI9DAUDNZERIWR9CPCAWBMRMJEWRPUVGRJE9']
	UID='AA'
	### We get all the request
	result=read_transaction(address,api,UID,public_key)
	##we only keep the legitimate request, and we remove double
	legitimate=list(set(get_legitimate_request(result)))
	

		
	