import subprocess
import re

def get_mac():
    try:
        ifconfig = subprocess.Popen(['ifconfig'], stdout=subprocess.PIPE)
        ifconfig = ifconfig.communicate()[0].decode('utf-8')
        # here we just run a regex in the mac address format
        mac = re.search(r'([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})', ifconfig)
        return mac.group(0)
    except Exception as e:
        return e


if __name__ == '__main__':
    print(get_mac())
