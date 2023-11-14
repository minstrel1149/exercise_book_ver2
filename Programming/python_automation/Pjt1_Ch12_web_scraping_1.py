from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import sys
from bs4 import BeautifulSoup as BS
import time

searchLink = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
options = Options()
options.add_argument('--windows-size=1600,900')
driver = webdriver.Chrome(options=options)

print('1끼지 완료')
time.sleep(3)

driver.get(searchLink + sys.argv[1])
page = driver.page_source
bs_obj = BS(page, 'html.parser')

print('2까지 완료')
time.sleep(3)

obj_list = bs_obj.find_all('a', {'class':'info'})
site_list = [x.get('href') for x in obj_list if x.get('href').startswith(f'https://n.news.naver')]

if len(site_list) > 0:
    print('\n'.join(site_list))
else:
    print('리스트에 항목이 없습니다.')

for site in site_list:
    driver.execute_script(f"window.open('{site}');")
    time.sleep(1)

for i in range(len(site_list)):
    driver.switch_to.window(driver.window_handles[i])
    time.sleep(1)

print('Process Done!')