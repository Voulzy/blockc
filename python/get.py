from iota import Iota, Address
from iota.codecs import TrytesDecodeError

# Declare an API object
api = Iota('https://nodes.devnet.iota.org:443', testnet=True)
txs = []

# Address to fetch data from
# Replace with your random generated address from Tutorial 2. to fetch the data
# that you uploaded.
addy = Address(b'ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9PREEIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDX')

print('Fetching data from the Tangle...')
# Fetch the transaction objects of the address from the Tangle
response = api.find_transaction_objects(addresses=[addy])
def getInfo(tag,info):
	if not response['transactions']:
	    return "Null"
	else:
	    for tx in response['transactions']:
	    	if tx.tag==tag+""+info:
		        txs.append(tx)
	return txs
