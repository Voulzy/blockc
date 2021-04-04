from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from rsa_signature import *





def sign_message(message,private_key):
	signature_base_64=sign(private_key,SHA256.new(message))
	return TryteString.from_bytes(signature_base_64)

def cast_message(value,private_key):
	###data for hash function
	data=(value+'tt').encode("utf-8")
	##message to store in the tangle
	message=TryteString.from_unicode(value)
	signature=sign_message(data,private_key)
	end=TryteString.from_unicode('?')
	message=message+signature+end
	return message


def send_request(value,address,private_key,api):
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



if __name__ == "__main__":
	file="../python/privatekey.pem"
	private_key=import_private_key(file)
	seed='CW9EUQWTNS9VCGQAQIHXMMWVZCEBCGKMUHYXBNEIGPQYYKTVRLBFJLEZHGMWYSRJKT9XAWSVLUNZE9YAX'
	api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)
	address='MRHDWPXVP9RVDBXNJRMJQQEREZTPAEUUDBPCBFQBLRUMQQI9DAUDNZERIWR9CPCAWBMRMJEWRPUVGRJE9'
	send_request('conso?',address,private_key,api)

