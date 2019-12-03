import sys
import time
from datetime import datetime

import requests

from main.models import Bus


def insert_bus():
    starttime = time.time()
    while True:
        try:
            data = requests.get('http://data.kzn.ru:8082/api/v0/dynamic_datasets/bus.json')
            for b in data.json():
                if b['data']['Marsh'] == '4':
                    bus = Bus()
                    bus.GaragNumb = b['data']['GaragNumb']
                    bus.Marsh = b['data']['Marsh']
                    bus.Graph = b['data']['Graph']
                    bus.Smena = b['data']['Smena']
                    bus.TimeNav = datetime.strptime(b['data']['TimeNav'], "%d.%m.%Y %H:%M:%S")
                    bus.Latitude = b['data']['Latitude']
                    bus.Longitude = b['data']['Longitude']
                    bus.Speed = b['data']['Speed']
                    bus.Azimuth = b['data']['Azimuth']
                    bus.save()
        except:
            print(sys.exc_info())

        time.sleep(60.0 - ((time.time() - starttime) % 60.0))
