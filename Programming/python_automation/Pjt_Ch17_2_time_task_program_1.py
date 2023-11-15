import requests
import os
import threading
from bs4 import BeautifulSoup as BS
from pathlib import Path

p1 = Path.cwd() / 'attachments'
os.makedirs(Path.cwd() / 'result_attachments' / 'xkcd2', exist_ok=True)
p2 = p2 = Path.cwd() / 'result_attachments' / 'xkcd2'

def downloadXkcd(startComic, endComic):
    for urlNum in range(startComic, endComic):
        print(f'Downloading page https://xkcd.com/{urlNum}..')
        res = requests.get(f'https://xkcd.com/{urlNum}')
        res.raise_for_status()

        bsObj = BS(res.text, 'html.parser')
        # #은 id속성
        comicElem = bsObj.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            print(f'Downloading image {comicUrl}..')
            res = requests.get(f'https:{comicUrl}')
            res.raise_for_status()

            with open(p2 / os.path.basename(comicUrl), mode='wb') as imgFile:
                for chunk in res.iter_content(100000):
                    imgFile.write(chunk)
    
downloadThreads = []

for i in range(0, 40, 10):
    start = i
    end = i + 9
    if start == 0:
        start = 1
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

print('Process Done!')