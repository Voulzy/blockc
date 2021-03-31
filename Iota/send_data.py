from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString

#privatekey of a car, should be remove later
seed = 'ESCIWUILOX9CCHPGMQUMDDGHFZZPFNYZCDYHMVYIDPOVSSHGWROCDIAVQNKPTOTCBPEIIQNUFXYSSEYUY'
#connexion to the devnet, from the seed 
api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)

address = 'NMSGHUHKOFCJSPCKBBDGQDJPRPWTGT9YCXDVBMUXTGSQAIZLAHSVNNOHEDQRXANVMLS9PWKPJVLCYYBNX'

tx = ProposedTransaction(
address=Address(address),
value = 10,
tag=Tag(b'AA'),
message=TryteString.from_unicode('wrong?100?')
) 
result = api.send_transfer(transfers=[tx] )
print('Bundle: ')
print(result['bundle'].tail_transaction.hash)
