


from ciscoconfparse import CiscoConfParse

def main():

    file = 'cisco.txt'

    config = CiscoConfParse(file)

    crypto_maps = config.find_objects_w_child(parentspec=r'crypto map CRYPTO',childspec=r'pfs group2')

    print "Crypto Maps with PFS group 2 mode: "

    for txt in crypto_maps:

        print "  {0}".format(txt.text)

    print


main()



