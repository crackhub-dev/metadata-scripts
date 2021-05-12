import requests as rq
import json
from sys import argv

appid = argv[1]

req = rq.get('https://store.steampowered.com/api/appdetails?appids=' + appid)

resp = req.json()

screenshots_len = len(resp[appid]['data']['screenshots'])


for screenshots in range(0, screenshots_len):
    screenshot = resp[appid]['data']['screenshots'][int(
        screenshots)]['path_full']
    img_tag = '<a href="' + screenshot + \
        '" target="_blank"> <img src="' + screenshot + '"/></a>'
    print(img_tag)
