


from ciscoconfparse import CiscoConfParse

def main():

    file = 'cisco.txt'

    config = CiscoConfParse(file)

    crypto_maps = config.find_objects(r"^crypto map CRYPTO")

    for cryptomaps in crypto_maps:

        print

        print cryptomaps.text

        for child in cryptomaps.children:

            print child.text

    print

main()



