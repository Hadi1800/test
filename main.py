import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas
import re
import random
import sys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import  time

class Bot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        driver.maximize_window()
        time.sleep(3)
        name = driver.find_element_by_name('username').send_keys(username)
        pas = driver.find_element_by_name('password').send_keys(password)
        btn_1 = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(5)
        btn_2 = driver.find_element_by_css_selector('button[type="button"]').click()
        time.sleep(5)
        btn_3 = driver.find_element_by_css_selector('button.HoLwm').click()
    def like(self):
        driver = self.driver
        time.sleep(2)
        driver.get('https://www.instagram.com/digikalacom/')
        post = driver.find_element_by_css_selector('a[href="/p/CWqrb2dAi-w/"]').click()
        i = 1
        while i<=5:
            time.sleep(5)
            if driver.find_elements_by_xpath('//*[contains(@aria-label,"Unlike")]'):
                time.sleep(3)
                driver.execute_script("document.getElementsByTagName('button')[6].click()")
            elif driver.find_elements_by_xpath('//*[contains(@aria-label,"like")]'):
                time.sleep(3)
                driver.find_element_by_class_name('fr66n').click()
                time.sleep(3)
                driver.execute_script("document.getElementsByTagName('button')[6].click()")
            i +=1
        driver.get('https://www.instagram.com/digikalacom/')





username = "hadi.zamanipour"
password = "H@di180066z63"
test =Bot(username,password)
test.login()
test.like()

# url1 = 'https://www.digikala.com/samsung-brand/mobile-phone/'
#
# titles = []
# for page in range(1,3):
#     page = requests.get(url1+str(page))
#     soup = BeautifulSoup(page.text, 'html.parser')
#     title = soup.select('div.c-product-box__content--row')
#     for t in title:
#         name = t.text
#         titles.append(name)



# def download(url) :
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links =soup.findAll('img',src = re.compile('.jpg'))
#     name=1
#     for info in links :
#         link = info.get('src')
#         # name = random.randrange(1,1000)
#         with requests.get(link,stream=True) as r:
#            name = name + 1
#            with open(str(name) + '.jpg','wb') as f:
#               for pic in r.iter_content(chunk_size=1024):
#                 f.write(pic)
#
#     if name == 100 :
#       sys.exit()
#
# download('https://www.digikala.com/samsung-brand/mobile-phone/')


# def download(url) :
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links =soup.findAll('a',href = re.compile('.mp4'))
#     for info in links :
#         link = info.get('href')
#         with requests.get(link,stream=True) as r:
#             with open('video_1.mp4','wb') as f:
#                 for video in r.iter_content(chunk_size=1024):
#                     f.write(video)
#
# download('https://video.varzesh3.com/video/241794/%D8%AF%D8%A7%D9%88%D8%B1%D9%BE%D9%86%D8%A7%D9%87-%D9%81%D8%AF%D8%B1%D8%A7%D8%B3%DB%8C%D9%88%D9%86-%D9%87%D8%B1%DA%A9%D8%A7%D8%B1%DB%8C-%D8%A7%D8%B2-%D8%AF%D8%B3%D8%AA%D8%B4-%D8%A8%D8%B1-%D9%85%DB%8C-%D8%A7%D9%93%DB%8C%D8%AF-%D8%A7%D9%86%D8%AC%D8%A7%D9%85-%D9%85%DB%8C-%D8%AF%D9%87%D8%AF')


# url = 'https://sibtoorsh.com/'
#
# titles = []
# prices = []
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# title = soup.select('h3.product-title')
# for t in title:
#     name = (t.text)
#     titles.append(name)
# price = soup.select('bdi')
# for p in price:
#     price = (p.text)
#     prices.append(price)
#
# product = {'title' : titles , 'price' : prices }
# data = pandas.DataFrame.from_dict(product, orient='index')
# data = data.transpose()
# writer = pandas.ExcelWriter('sibtoorsh.xlsx')
# data.to_excel(writer)
# writer.save()

#
#
# import requests
# from bs4 import BeautifulSoup
# import pandas
#
#
# url = 'https://www.digikala.com/samsung-brand/mobile-phone/'

# titles = []
# prices = []
# for page in range(1,3):
#     page = requests.get(url+str(page))
#     soup = BeautifulSoup(page.text, 'html.parser')
#     title = soup.select('div.c-product-box__content--row')
#     for t in title:
#         name = t.text
#         titles.append(name)
#     price = soup.select('div.c-price__value-wrapper')
#     for p in price:
#         pr = p.text.strip()
#         prices.append(pr)
#
# product = {'Title': titles, 'Price' : prices}
# data = pandas.DataFrame.from_dict(product, orient='index')
# data = data.transpose()
# writer = pandas.ExcelWriter('dg.xlsx')
# data.to_excel(writer)
# writer.save()



