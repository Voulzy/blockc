from iota import Iota
from iota import Tag 

print ("Connexion to the iota devnet...")

api = Iota('https://nodes.devnet.iota.org:443', testnet = True)

print( "Get all the transaction from the concessionaire address..")

address= ['NMSGHUHKOFCJSPCKBBDGQDJPRPWTGT9YCXDVBMUXTGSQAIZLAHSVNNOHEDQRXANVMLS9PWKPJVLCYYBNXYITYTJKJD']

transactions = api.find_transaction_objects(addresses=address)

for transaction in transactions['transactions']:
  # Ignore input transactions; these have cryptographic signatures,
  # not human-readable messages.
  if transaction.value < 0:
    continue

  print(f'Message from {transaction.hash}:')

  message = transaction.signature_message_fragment
  Tag_t=transaction.tag
  if message is None:
    print('(None)')
  else:
    print(message.decode())
    print('\n'+bytes(Tag_t).decode())
