from iota import Iota
from iota import Tag 
import numpy as np


#####definition des variables a récuperer####
km=[]
conso=[]
usure=[]

########### Fin definition variable


print ("Connexion to the iota devnet...")

api = Iota('https://nodes.devnet.iota.org:443', testnet = True)

###### A utiliser pour saisi manuel de l'uid

#input=input("Quel est l'UID de la voiture ?")
#print("UID saisi : ",input) 

#####

print( "Get all the transaction from the concessionaire address..")
address= ['NMSGHUHKOFCJSPCKBBDGQDJPRPWTGT9YCXDVBMUXTGSQAIZLAHSVNNOHEDQRXANVMLS9PWKPJVLCYYBNXYITYTJKJD']

## get all transaction done to the adress
transactions = api.find_transaction_objects(addresses=address)
UID='AA9999999999999999999999999'
print("Parcours des transaction")
for transaction in transactions['transactions']:
  # Ignore input transactions; these have cryptographic signatures,
  # not human-readable messages.
  if transaction.value < 0:
    continue

  print(f'Hash : {transaction.hash}:')
  message = transaction.signature_message_fragment
  Tag_t=transaction.tag
  if message is None:
    print('(None)')
  else :
    if Tag_t==UID :
        code=message.decode().split('?')[0]
        if code=='km':
          print(int(message.decode().split('?')[1]))
          km.append(int(message.decode().split('?')[1]))
          print(km)
        if code=='conso' :
          print(int(message.decode().split('?')[1]))

