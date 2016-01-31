import yaml
import json


def main():
    
    yaml_file = 'my_yaml.yml'
    json_file = 'my_json.json'

    net_dict = {'ip_addr' : '192.168.1.214', 'model' : 'wlc', 'manufacturer' : 'Cisco', 'model': '2504'}
    
    net_list = ['test_strings','1','2','3', net_dict, 'python', 'neteng']
    
    with open(yaml_file, "w") as f:
        f.write(yaml.dump(net_list, default_flow_style=False))

    with open(json_file, "w") as f:
        json.dump(net_list, f)


main() 




