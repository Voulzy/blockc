from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from rsa_signature import *
#privatekey of a car, should be remove later
seed = 'ESCIWUILOX9CCHPGMQUMDDGHFZZPFNYZCDYHMVYIDPOVSSHGWROCDIAVQNKPTOTCBPEIIQNUFXYSSEYUY'
#connexion to the devnet, from the seed 
api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)
file="../python/privatekey.pem"
address = 'XJWGTWXL9JBKRGXONOXCIFLALYGAHFQKKSPFADNMJLDOZYNDWCPVUWJCK9OYBUNYNWVHQDKOHVDZE9PTD'
private_key=import_private_key(file)

input_data=input("Quel est votre data a envoyé ?")
input_tag=input("Quel est votre tag de voiture ?") 

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
tag=Tag(input_tag),
message=message
) 
result = api.send_transfer(transfers=[tx] )
print('Bundle: ')
print(result['bundle'].tail_transaction.hash)
