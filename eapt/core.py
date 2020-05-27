from urllib.request import urlopen
import json
import ssl

def currentIpInfo():
    info = None
    with urlopen('http://free.ipwhois.io/json/') as response:
        data = response.read().decode('utf-8')
        info = json.loads(data)
    return info