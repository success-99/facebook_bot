import requests
import json

# link = "https://fb.watch/iNjp9wReOZ/"
def facebook(linkf):
    url = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"

    querystring = {"url": linkf}

    headers = {
        "X-RapidAPI-Key": "ec416768d4msh1192262c9228acbp1514bbjsn6e79cab64711",
        "X-RapidAPI-Host": "facebook-reel-and-video-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    natija5 = json.loads(response.text)


    #
    #
    if 'error' in natija5:
        return 'bed'
    else:
        return natija5['links']['Download High Quality']
        # for i in natija5['formats']:
        #     if i['ext'] == 'mp4' and i['quality'] == 0:
        #         return i['url']

    #








# print(facebook(link))
