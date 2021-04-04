from iota import Iota

seed= 'CW9EUQWTNS9VCGQAQIHXMMWVZCEBCGKMUHYXBNEIGPQYYKTVRLBFJLEZHGMWYSRJKT9XAWSVLUNZE9YAX'

api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)

security_level = 2
address = api.get_new_addresses(index=0, count=1, security_level = security_level)['addresses'][0]

is_spent = api.were_addresses_spent_from([address])['states'][0]

if is_spent:
    print('Address %s is spent!' % address )
else:
    print('Your address is: %s' % address )


