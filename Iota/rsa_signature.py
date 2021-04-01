import Crypto
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import base64


def sign (key,data):
	return base64.b64encode(pkcs1_15.new(key).sign(data))

def verify (key,data,sign):
	return pkcs1_15.new(key).verify(data,base64.b64decode(sign))

#print("test")
## On récupere clé publique (format pkcs1)
def import_private_key():
	with open('../python/privatekey.pem',mode='rb') as private_file:
        	key_private=private_file.read()
        	private_key=Crypto.PublicKey.RSA.import_key(key_private)
        	return private_key
def import_public_key():
	with open('../python/publickey.pem', mode='rb') as public_file:
		key_data = public_file.read()
		public_key = Crypto.PublicKey.RSA.import_key(key_data)
		return public_key
## On récupère clé privé (pkcs1? avec openssl)
#with open('../python/privatekey.pem',mode='rb') as private_file:
#	key_private=private_file.read()
#	private_key=Crypto.PublicKey.RSA.import_key(key_private)
#	print(private_key)
## On signe (encodage utf8 obligatoire)
#data='km150'.encode("utf-8")
#data=SHA256.new(data)

#private_key=import_private_key()
#signature=sign(private_key,data)
#print(signature)
### On change le message (vérification que cela echoue, si on change pas, on verifie que ca marche
#data='toto'.encode("utf-8")
#data=SHA256.new(data)
#public_key=import_public_key()


##None si OK, raise erreur si not ok
#print(verify(public_key,data,signature))
