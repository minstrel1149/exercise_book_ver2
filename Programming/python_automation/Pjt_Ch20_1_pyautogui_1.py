from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
import time

options = Options()
options.add_argument('--window-size=1600,900')
driver = webdriver.Chrome(options=options)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
           ]

driver.get('https://autbor.com/form')

pag.PAUSE = 3
print('Ensure that the browser window is active and the form is loaded')

for person in formData:
    print('5 seconds pause to let user press ctrl c')
    time.sleep(5)

    print(f'Entering {person["name"]} info..')

    pag.write(['\t', '\t', '\t', '\t'])
    pag.write(person['name'] + '\t', 0.1)
    pag.write(person['fear'] + '\t', 0.1)

    if person['source'] == 'wand':
        pag.write(['down', 'enter', '\t'], 0.3)
    elif person['source'] == 'amulet':
        pag.write(['down', 'down', 'enter', '\t'], 0.3)
    elif person['source'] == 'crystal ball':
        pag.write(['down', 'down', 'down', 'enter', '\t'], 0.3)
    elif person['source'] == 'money':
        pag.write(['down', 'down', 'down', 'down', 'enter', '\t'], 0.3)
    
    if person['robocop'] == 1:
        pag.write(['right', 'left', '\t', '\t'], 0.3)
    elif person['robocop'] == 2:
        pag.write(['right', '\t', '\t'], 0.3)
    elif person['robocop'] == 3:
        pag.write(['right', 'right', '\t', '\t'], 0.3)
    elif person['robocop'] == 4:
        pag.write(['right', 'right', 'right', '\t', '\t'], 0.3)
    elif person['robocop'] == 5:
        pag.write(['right', 'right', 'right', 'right', '\t', '\t'], 0.3)
    
    pag.write(person['comments'] + '\t')

    time.sleep(0.5)
    pag.press('enter')

    print('submitted form.')
    time.sleep(5)

    pag.write(['\t', 'enter'])

print('Process Done!')