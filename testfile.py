import pandas as pd
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# import numpy as np
from bs4 import BeautifulSoup
# import os
import time
import parse_datarade as pdr


datarade_url = 'https://datarade.ai/'
xlpath = '/Users/leo_z/Downloads/Data-Hunters Data Providers Connections.xlsx'
# data_providers = pd.read_excel(xlpath,sheet_name=0).fillna('').dropna()
data_categories = pd.read_excel(xlpath,sheet_name=1).fillna('')
use_cases = pd.read_excel(xlpath,sheet_name=2).fillna('')
datasets = pd.read_excel(xlpath,sheet_name=6).fillna('').dropna()
classname_alternative = 'provider-profile__alternative__header-name'
datasets_list = datasets['post_title'].unique()
# print(datasets_list)
# print(len(datasets_list))
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-infobars')
driver = webdriver.Chrome('/Users/leo_z/Documents/GitHub/emboodo/chromedriver')



driver.get(datarade_url)
driver.find_element_by_xpath('/html/body/div[1]/header/div[1]/div/div/form/div/div[1]/input[2]').send_keys(datasets_list[0])#.send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/header/div[1]/div/div/form/div/div[2]/a[1]').click()
s = driver.page_source
soup = BeautifulSoup(s, features="html.parser")
data_cat_list = pdr.get_data_cat_list(soup)
usecase_list = pdr.get_usecase_list(soup)
print(data_cat_list)
print(usecase_list)
# related_list = pick_existing_entries(related_list_raw,providers)
