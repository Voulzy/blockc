import Crypto
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256



def sign (key,data):
	return pkcs1_15.new(key).sign(data)

def verify (key,data,sign):
	return pkcs1_15.new(key).verify(data,sign)

print("test")
## On récupere clé publique (format pkcs1)
with open('publickey.pem', mode='rb') as public_file:
	key_data = public_file.read()
	public_key = Crypto.PublicKey.RSA.import_key(key_data)
## On récupère clé privé (pkcs1? avec openssl)
with open('privatekey.pem',mode='rb') as private_file:
	key_private=private_file.read()
	private_key=Crypto.PublicKey.RSA.import_key(key_private)
	print(private_key)
## On signe (encodage utf8 obligatoire)
data='Babar'.encode("utf-8")
data=SHA256.new(data)

signature=sign(private_key,data)
### On change le message (vérification que cela echoue, si on change pas, on verifie que ca marche
#data='toto'.encode("utf-8")
#data=SHA256.new(data)



##None si OK, raise erreur si not ok
print(verify(public_key,data,signature))
