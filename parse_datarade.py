# import requests
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import numpy as np
from bs4 import BeautifulSoup
import os
import time


# options = Options()
# options.add_argument('--disable-logging')
# options.add_argument('--incognito')
# options.add_argument('--disable-infobars')
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1300,800")
# options.add_argument("--disable-dev-shm-usage")
# #options.add_argument("--headless")
# #options.add_argument("--host-resolver-rules=MAP www.google-analytics.com 127.0.0.1")
# options.add_argument("no-default-browser-check")
# options.add_argument("no-first-run")

url = 'https://datarade.ai/data-providers/'
profile = '/profile'
alternatives = '/alternatives'

classname_alternative = 'provider-profile__alternative__header-name'
classname_datacat = "tag-label tag-label--green"
classname_usecase = "tag-label tag-label--blue"

xlpath = '/Users/leo_z/Downloads/Data-Hunters Data Providers Connections.xlsx'
data_providers = pd.read_excel(xlpath,sheet_name=0).fillna('').dropna()
# data_providers = data_providers.dropna(subset=data_providers.columns)
# print(data_providers.head(10))
data_categories = pd.read_excel(xlpath,sheet_name=1).fillna('')
use_cases = pd.read_excel(xlpath,sheet_name=2).fillna('')

def get_unique(df,column):
    return [i.lower() for i in df[column].dropna().unique()]

def map_categories(df):
    return {row['Datarade'].lower():row['Datarade New'] for i,row in df.iterrows()}

def map_use_cases(df):
    return {row['datarade']:row['datarade new'] for i,row in df.iterrows()}


def get_list_of_texts_by_class(soup, class_name):    
    datacat = soup.findAll(attrs={"class" : class_name}) 
    return[i.text for i in datacat]


def pick_existing_entries(list, blueprint):
    return [i for i in list if i.lower() in blueprint]


def checked_for_existence(list_, d):
    new_list = []
    for i in list_:
        if i.lower() in d.keys():
            new_list.append(d[i.lower()])
        elif i.lower() in [i.lower() for i in list(d.values())]:
            new_list.append(i)
    return new_list

providers = (get_unique(data_providers, 'post_title'))
categories = map_categories(data_categories)
cases = map_use_cases(use_cases)

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-infobars')
driver = webdriver.Chrome('/Users/leo_z/Documents/GitHub/emboodo/chromedriver')
driver2 = webdriver.Chrome('/Users/leo_z/Documents/GitHub/emboodo/chromedriver',chrome_options=chrome_options)


def get_data_cat_list(soup):
    return get_list_of_texts_by_class(soup,classname_datacat)

def get_usecase_list(soup):
    return get_list_of_texts_by_class(soup,classname_usecase)


def get_related_data_providers(driver, provider):
    related_url = url + provider + alternatives
    driver.get(related_url)
    s = driver.page_source
    soup = BeautifulSoup(s, features="html.parser")
    related_list_html = soup.findAll(attrs={"class" : classname_alternative})
    related_list_raw = [i.text for i in related_list_html]
    related_list = pick_existing_entries(related_list_raw,providers)
    return related_list


def table_row(row):
    name = row['post_title']
    name = name.lower().replace(' ','-')
    descr = row['post_content'].replace('\n','').replace('\r','')
    descr2 = row['post_excerpt'].replace('\n','').replace('\r','')
    row['post_content'] = descr
    row['post_excerpt'] = descr2
    print('provider ', name)
    profile_url = url + str(name)+ profile
    driver.get(profile_url)
    s = driver.page_source
    text_of_ban = driver.find_element("xpath","/html/body")
    if text_of_ban.text =="Too many requests in a given amount of time. We employ rate limiting to ensure the stability of our services to all users. If you think this is a mistake, contact us at platform@datarade.ai":
        raise ValueError('banned, switch to a different VPN')

    soup = BeautifulSoup(s, features="html.parser")
    try:
        data_cat_list = get_data_cat_list(soup)
    except Exception:
        data_cat_list = ['no data']
    try:
        usecase_list = get_usecase_list(soup)
    except:
        usecase_list = ['no data']
    time.sleep(1)
    try: 
        related_list = get_related_data_providers(driver2, name)
    except:
        related_list = ['no data']
    row['related_data_providers'] = ','.join(related_list)
    row['related_use_cases'] = ','.join(checked_for_existence(usecase_list,cases))
    row['categories'] = ','.join(checked_for_existence(data_cat_list, categories))
    return row


def handle_providers_table(df, batch_size, start):
    cnt = 0
    df = df.dropna()
    # print(df.head(15))
    df_new = pd.DataFrame(columns=df.columns)
    df_list = []
    for num,i in df.iloc[start:start+batch_size].iterrows():
        cnt +=1
        new_row = table_row(i)
        # print('NEWROW')
        # print(new_row)
        df_list.append(new_row)
    df_new = pd.DataFrame(df_list)
    # print(df_new)
    # print('DFNEW')
    # print('CNT',cnt)
    return df_new

batch_size = 1

try:
    with open("current.txt", "r") as text_file:
        tx = text_file.read()
        n0 = int(tx)
except:
        n0=0

while n0<len(data_providers):
    n0+=batch_size   
    print(n0)
    df_new = handle_providers_table(data_providers,batch_size,n0)
    hdr = (n0 == 0)
    
    # print(df_new.iloc[0])
    df_new.to_csv('newdf.csv',mode='a',header=hdr,index = False)
    with open("current.txt", "w") as text_file:
        text_file.write(str(n0))

