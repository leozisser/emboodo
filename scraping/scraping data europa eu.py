from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
import csv
from unidecode import unidecode
import autoit
import random
import os
from datetime import timedelta, datetime
import time
from statistics import mean
import re
from textblob import TextBlob
from langdetect import detect
from progress.bar import IncrementalBar
import langid
LOGGER.setLevel(logging.WARNING)
options = Options()
#options.add_argument('--proxy-server=176.9.119.170:1080	')
#options.add_argument("no-sandbox")
options.add_argument('--disable-logging')
options.add_argument('--incognito')
options.add_argument('--disable-infobars')
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1300,800")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")
#options.add_argument("--host-resolver-rules=MAP www.google-analytics.com 127.0.0.1")
options.add_argument("no-default-browser-check")
options.add_argument("no-first-run")
def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element("xpath",xpath)
    except Exception:
        return False
    return True
def check_exists(driver,way,name):
    try:
        driver.find_element(way,name)
    except Exception:
        return False
    return True
i = 0
i_number = open(r'C:\Users\Анатолий\Desktop\python\i.txt', 'r')
for lines in i_number:
    i = int(lines)
print(i)
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=options
)
#i = 12033 + 563 + 1130 + 500 + 966 +1087 + 81 + 5 + 10 + 13
driver.get("https://data.europa.eu/data/datasets?locale=en&page="+str(i)+"")
driver.maximize_window()
f = open(r'C:\Users\Анатолий\Desktop\python\scraping data europa eu.txt', 'a')

number_of_all = 0
not_loaded = 0
avg_time_for_all = []

while int(i) < (89174):
    
    start_time = time.time()
    driver.delete_all_cookies()
    check_if_page_loaded = check_exists(driver,"class name","alert")
    time.sleep(0.2)
    if check_if_page_loaded == True and driver.find_element("class name","alert").text.find("datasets ") != -1:
        
        #print(driver.find_element("class name","alert").text.find("datasets "))
        data_set_boxes = driver.find_elements("class name","data-info-box")
        
        for one_data_set in data_set_boxes :
            try:
                title_text = (one_data_set.find_element("class name","card-header").text)
            except:
                title_text = "Аааааааааааа"
            try:
                description_text = (one_data_set.find_element("class name","card-text").text)
            except Exception:
                description_text = "Аааааааааа"
            
            link = one_data_set.find_element("class name","text-dark").get_attribute("href")
            #print((langid.classify(title_text))[0])
            if langid.classify(title_text)[0] == langid.classify(description_text)[0] and langid.classify(title_text)[0]  == "en":
                print(title_text)
                print(description_text)
                print(link)
                number_of_all += 1
                f.write(link + "\n")
                print()
                print()
        driver.find_element("class name","next-button").click()
        driver.find_element("xpath","/html/body")
        
        os.system('CLS')
        print(i)
        full_time_text= ""
        avg_time_for_one =(time.time() - start_time)
        avg_time_for_all.append(avg_time_for_one)
        avg_time = mean(avg_time_for_all)
        full_time_text = str(full_time_text) + "Среднее время выполнения :" + str(avg_time) + "\n"
        full_time_in_seconds = int(avg_time * ((89174) - i))
        full_time_in_minutes = full_time_in_seconds //60
        ost_v_sec = full_time_in_seconds %60
        full_time_in_hours = full_time_in_minutes //60
        ost_v_min = full_time_in_minutes %60
        full_time_in_days = full_time_in_hours // 24
        ost_v_hours = full_time_in_hours% 24
        full_time_text = str(full_time_text) + "Осталось времени "  +str(full_time_in_days) + " дней " + str(ost_v_hours) + " ч " + str(ost_v_min) + " мин "  + str(ost_v_sec) +  " сек" +"\n"
        
        full_time_text = full_time_text + "Будет закончено примерно " + str((datetime.now() + timedelta(seconds = full_time_in_seconds)))
        print(full_time_text)
        print(number_of_all)
        print(not_loaded)
        i_number = open(r'C:\Users\Анатолий\Desktop\python\i.txt', 'w')
        i += 1
        not_loaded+= 1
        i_number.write(str(i))
        i_number.close()
    else:
        time.sleep(0.01)
    
    
# mx-auto mt-3 mb-3   