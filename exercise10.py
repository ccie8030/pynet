

import re
from ciscoconfparse import CiscoConfParse

def main():

    file = 'cisco.txt'

    config = CiscoConfParse(file)

    crypto_maps = config.find_objects_wo_child(parentspec=r'crypto map CRYPTO',childspec=r'AES')

    print "Crypto Maps not using AES: "

    for txt in crypto_maps:
        for child in txt.children:
            if 'transform' in child.text:
                match = re.search(r"set transform-set (.*)$", child.text)
                encryption = match.group(1)

        print "  {0} >>> {1}".format(txt.text.strip(), encryption)

    print


main()



