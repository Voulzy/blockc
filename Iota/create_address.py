from iota import Iota

seed= 'BEAXWJOTVBHGUXNRZSAYBRJSXLXPCQOIQYIZKPHDAWEGKTKQLHLXJPXPGKUDJTYXZAHHNTYXUJUCABTTY'

api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)

security_level = 2
address = api.get_new_addresses(index=1, count=1, security_level = security_level)['addresses'][0]

is_spent = api.were_addresses_spent_from([address])['states'][0]

if is_spent:
    print('Address %s is spent!' % address )
else:
    print('Your address is: %s' % address )


