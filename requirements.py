import requests as rq
import json
from sys import argv

appid = argv[1]

req = rq.get('https://store.steampowered.com/api/appdetails?appids=' + appid)

resp = req.json()

requirements = resp[appid]['data']['pc_requirements']['minimum']
print(requirements)
