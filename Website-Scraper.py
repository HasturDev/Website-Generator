from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re


link_list = []
secondary_pages = []
tag_list = []



session = webdriver.Chrome(r"C:\Users\i_miz\Downloads\chromedriver_win32\chromedriver.exe")

session.get('https://pyatl.dev')
time.sleep(3)
bs = BeautifulSoup(session.page_source, 'lxml')
print(bs.find_all('a'))
for i in bs.find_all('a', attrs={'href': re.compile("^https://")}):
    print (i.get('href'))
    link_list.append(i.get('href'))
session.close()


