from iota import Iota,TryteString,Address,Tag,ProposedTransaction
from pprint import pprint

api = Iota('https://nodes.devnet.iota.org:443', testnet=True)


message=TryteString.from_unicode('Hello world')
adress="ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9PREEIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDX"


tag=Tag(b'MY9FIRST9TAG')

tx = ProposedTransaction(
	address = Address(adress),
	message = message,
	value = 0
)
result = api.send_transfer([tx])

pprint('Check your transaction on the Tangle!')
pprint('https://utils.iota.org/transaction/%s/devnet' % result['bundle'][0].hash)

#ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9PREEIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDX
