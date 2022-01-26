from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.common.keys import Keys
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
from alive_progress import alive_bar
from progress.bar import IncrementalBar
LOGGER.setLevel(logging.WARNING)
options = Options()
#options.add_argument('--proxy-server=176.9.119.170:1080	')
options.add_argument("no-sandbox")
#options.add_argument("--disable-gpu")
options.add_argument("--window-size=1300,800")
options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--headless")
#options.add_argument("--host-resolver-rules=MAP www.google-analytics.com 127.0.0.1")
options.add_argument("no-default-browser-check")
options.add_argument("no-first-run")
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=options
)

up = 0   
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
fieldnames1 = ["Data Set link","Data Vendor Logo", "Name of the dataset","Data Vendor Name","Description","Full Description","Data Attributes","Use cases","Data Categories","Related Products","FAQ"]

#with open(r"C:\Users\Анатолий\Desktop\python\scraping.csv", 'w') as f:
    #writer = csv.DictWriter(f, fieldnames = fieldnames1, delimiter = ';')
    #writer.writeheader()

driver.get("https://www.google.com/")
driver.maximize_window()
fullfile = []
autoit.win_wait_active("Google - Google Chrome")
#time.sleep(5)
f = open(r"C:\Users\Анатолий\Desktop\python\scraping data europa eu.txt")
avg_time_for_all = []
number = 0
list_number = 18
list_text = []
for lines in f:
    list_text.append(lines)
#bar = IncrementalBar('Выполнено', max = len(list_text))
print("started")
#with alive_bar(len(list_text)) as bar:
while list_number<= len(list_text):
    flag_of_ready = False
    start_time = time.time()
    number += 1
    one_row = []
    
    print(list_text[list_number])
    #driver.execute_script("window.open("+"'"+(list_text[list_number])+"'"+");")
    #driver.find_element(By.linkText(list_text[list_number])).sendKeys(selectLinkOpeninNewTab)
    #driver.execute_script("window.open('"+(list_text[list_number])+"')")
    driver.get(list_text[list_number])
    flag_of_ready = False
    one_row.append(list_text[list_number])
    #time.sleep(2)
    
    #text_of_ban = driver.find_element("xpath","/html/body")
    #print(text_of_ban.text[0:10])
    #if text_of_ban.text !="Too many requests in a given amount of time. We employ rate limiting to ensure the stability of our services to all users. If you think this is a mistake, contact us at platform@datarade.ai":
    testing_on_404 = ""
    
    print(list_number, " " ,check_exists(driver,"class name","container-fluid"))
    if check_exists(driver,"class name","container-fluid") == True:
        testing_on_404 = driver.find_element("class name","container-fluid")
        testing_on_404 = testing_on_404.text
        #print(testing_on_404.text)
    #print(driver.find_element("class name","container-fluid ").text)
    print("404 : ",testing_on_404)
    if testing_on_404.find( != "Error 404": 
        while flag_of_ready == False:
            
            flag_of_ready = check_exists_by_xpath(driver,"/html/body/div/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]")
        
    
            ##time.sleep(10)
        logo_check = check_exists(driver,"xpath","/html/body/div/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]")
        #col-10
        if logo_check == True: 
            time.sleep(0.6)
            logo = driver.find_element("xpath","/html/body/div/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]")
            logo = logo.find_element("tag name","img")
            ##print(logo_src)
            logo_src = logo.get_attribute("src")
            logo_src = logo_src.strip()
            logo_src = logo_src.replace("\n","")
            #print(logo_src[0:20])
            one_row.append(logo_src)
            ##time.sleep(10)
        else:
            one_row.append("-")
        data_set_name_check = check_exists(driver,"class name","offset-lg-1")
       
        if data_set_name_check == True: 
            data_set_name_upper_elem = driver.find_element("class name","offset-lg-1")
            data_set_name_elem = data_set_name_upper_elem.find_element("tag name","h1")
            data_set_name = data_set_name_elem.text
            data_set_name = data_set_name.strip()
            data_set_name = data_set_name.replace("\n","")
            data_set_name = unidecode(data_set_name)
            #print(data_set_name[0:20])
            one_row.append(data_set_name)
        else:
            #data_set_name_elem = driver.find_element("class name","offset-lg-1")
            one_row.append("-")
        data_vendor_name_check = check_exists(driver,"xpath","/html/body/div/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/span[2]")
        #print(data_vendor_name_check)
        #app > div > div.site-wrapper > div.d-flex.flex-column.p-0.bg-transparent.content > div > div:nth-child(1) > div > div > div:nth-child(2) > div.row.mt-1 > div:nth-child(2)
        if data_vendor_name_check == True: 
            data_vendor_name_elem = driver.find_element("xpath","/html/body/div/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/span[2]")
            data_vendor_name = data_vendor_name_elem.text
            #print(data_vendor_name)
            #data_vendor_name = data_vendor_name.split(":")
            #data_vendor_name = data_vendor_name[1]
            ##print(data_vendor_name)
            data_vendor_name = data_vendor_name.strip()
            data_vendor_name = data_vendor_name.replace("\n","")
            data_vendor_name = unidecode(data_vendor_name)
            #data_vendor_name = re.sub("[^A-Za-z]", "", data_vendor_name)
            #print(data_vendor_name)
            one_row.append(data_vendor_name)
        else:
            one_row.append("-")
        ##time.sleep(10)
        description_check = check_exists(driver,"class name","markdown-content")
        if description_check == True: 
            description_elem = driver.find_element("class name","markdown-content")
            description = description_elem.text
            ##print(description)
            ##print()
            ##print()
            description = description.strip()
            description = description.replace("\n","")
            description = unidecode(description)
            #description = re.sub("[^A-Za-z]", "", description)
            #print(description)
            one_row.append(description)
        else:
            one_row.append("-")
        download_first_check = check_exists(driver,"class name","position-relative")
        if download_first_check == True: 
            download_first_elem = driver.find_elements("class name","position-relative")
            i = 0
            while i <len(download_first_elem):
                print(download_first_elem[i].text.replace("keyboard_arrow_down","").strip().lower())
                print()
                if download_first_elem[i].text.replace("keyboard_arrow_down","").strip().lower() == "download":
                    download_first_elem[i].click()
                    check_dropdownenu = check_exists(driver,"class name","dropdownMenu")
                    print(check_dropdownenu)
                    if check_dropdownenu == True:
                        elem_dropdownenu = driver.find_element("class name","dropdownMenu")
                        download_link = elem_dropdownenu.find_element("tag name","small")
                        download_link.click()
                        #px-2
                    else:
                        pass
                    i = len(download_first_elem) + 1
                else:
                    pass
                
                i+= 1
            #time.sleep(5)
            #time.sleep(25)
            ##print(description)
            ##print()
            ##print()
            description = description.strip()
            description = description.replace("\n","")
            description = unidecode(description)
            #description = re.sub("[^A-Za-z]", "", description)
            #print(description)
            one_row.append(description)
        else:
            one_row.append("-")
        '''
        full_text_check = check_exists(driver,"class name","product-content__description")
        if full_text_check == True: 
            full_text_elem = driver.find_element("class name","product-content__description")
            full_text = full_text_elem.text
            ##print(full_text)
            full_text = full_text.strip()
            full_text = full_text.replace("\n","")
            full_text = unidecode(full_text)
            #full_text = re.sub("[^A-Za-z]", "", full_text)
            one_row.append(full_text)
        else:
            one_row.append("-")
        
        data_attributes_check = check_exists(driver,"class name","product-content__attributes")
        if data_attributes_check == True:
            data_attributes_elem = driver.find_element("class name","product-content__attributes")
            data_attributes = data_attributes_elem.text
            ##print(data_attributes)
            data_attributes = data_attributes.strip()
            data_attributes = data_attributes.replace("\n","")
            data_attributes = unidecode(data_attributes)
            #data_attributes = re.sub("[^A-Za-z]", "", data_attributes)
            one_row.append(data_attributes)
        else:
            one_row.append("-")
            ##print("no")
        
        use_cases_check = check_exists(driver,"class name","product-content__use_cases")
        if use_cases_check == True: 
            use_cases_elem = driver.find_element("class name","product-content__use_cases")
            use_cases = use_cases_elem.text
            ##print(use_cases)
            use_cases = use_cases.strip()
            use_cases = use_cases.replace("\n","")
            use_cases = unidecode(use_cases)
            #use_cases = re.sub("[^A-Za-z]", "", use_cases)
            one_row.append(use_cases)
        else:
            one_row.append("-")
        '''
        #similar_datasets = driver.find_element("class name","nav-link")
        time.sleep(2)
        data_categories_upper_element = driver.find_element("class name",'menu')
        print(type(data_categories_upper_element))
        time.sleep(0.5)
        flag_0 = 0
        while flag_0 == 0:
            try:
                data_categories_upper_element.find_element("xpath",'//span[contains(text(), "Categories")]').click()
                
            except:
                flag_0 = 0
            else:
                flag_0 = 1
        data_categories_upper_element.find_element("xpath",'//span[contains(text(), "Categories")]').click()
        print(1)
        data_categories_check = check_exists(driver,"class name","categories")
        if data_categories_check == True: 
            data_categories_elem = driver.find_element("class name","categories")
            data_categories = data_categories_elem.text
            ##print(data_categories)
            data_categories = data_categories.strip()
            data_categories = data_categories.replace("\n","")
            data_categories = unidecode(data_categories)
            #data_categories = re.sub("[^A-Za-z]", "", data_categories)
            #print(data_categories)
            one_row.append(data_categories)
        else:
            one_row.append("-")
        '''
        related_products_check = check_exists(driver,"class name","vertical-product-card")
        if related_products_check == True: 
            related_product_amount = driver.find_elements("class name","vertical-product-card")
            full_related_products_info = ""
            for headers in related_product_amount:
                names = headers.find_element("class name","vertical-product-card__title").text
                names = names.split("by ")
                names = names[0]
                ##print(names)
                hrefs = headers.find_element("tag name","a")
                hrefs = hrefs.get_attribute("href")
                full_related_products_info = str(full_related_products_info) + str(names) + " : " + str(hrefs) + ","
                full_related_products_info = full_related_products_info.strip()
                full_related_products_info = full_related_products_info.replace("\n","")
                full_related_products_info = unidecode(full_related_products_info)
            ##print(full_related_products_info)
            one_row.append(full_related_products_info)
                
        else:
            one_row.append("-")
        #/html/body/div[1]/main/div/div[3]/div/div/div[1]/section[10]/div
        faq_check = check_exists(driver,"class name","dtrd-faq")
        if faq_check == True: 
            faq_elem = driver.find_element("class name","dtrd-faq")
            faq = faq_elem.text
            ##print(faq)
            faq = faq.strip()
            faq = faq.replace("\n","")
            faq = unidecode(faq)
            #faq = re.sub("[^A-Za-z]", "", faq)
            one_row.append(faq)
            
        else:
            one_row.append("-")
        '''
        
        with open(r"C:\Users\Анатолий\Desktop\python\scraping.csv", 'a') as qwerty: 
            writer = csv.writer(qwerty, delimiter = ";")
            writer.writerow(one_row)
        #print(str(number) +" " + str(len(list_text)))
        list_number+=1
        #bar()
        #bar.next()
        os.system('CLS')
        full_time_text= ""
        avg_time_for_one =(time.time() - start_time)
        avg_time_for_all.append(avg_time_for_one)
        avg_time = mean(avg_time_for_all)
        full_time_text = str(full_time_text) + "Среднее время выполнения :" + str(avg_time) + "\n"
        full_time_in_seconds = int(avg_time * (len(list_text)) - list_number)
        full_time_in_minutes = full_time_in_seconds //60
        ost_v_sec = full_time_in_seconds %60
        full_time_in_hours = full_time_in_minutes //60
        ost_v_min = full_time_in_minutes %60
        full_time_in_days = full_time_in_hours // 24
        ost_v_hours = full_time_in_hours% 24
        full_time_text = str(full_time_text) + "Осталось времени "  +str(full_time_in_days) + " дней " + str(ost_v_hours) + " ч " + str(ost_v_min) + " мин "  + str(ost_v_sec) +  " сек" +"\n"
        
        full_time_text = full_time_text + "Будет закончено примерно " + str((datetime.now() + timedelta(seconds = full_time_in_seconds)))
        print(full_time_text)
        print(list_number, "из", len(list_text))
        for f in one_row:
            print(f[0:50])
        time.sleep(2)   
    else:
        #bar()
        list_number+=1
        
        ##print()
        
        '''
        else:
            driver.close()
            autoit.win_activate("StrongVPN.com - Setup Instructions - Google Chrome")
            autoit.win_wait_active("StrongVPN.com - Setup Instructions - Google Chrome")
            autoit.mouse_click("left",482, 640)
            for i in range(0,50):
                autoit.send("{down}")
            #time.sleep(0.1)
            up+=1
            for f in range(0,up):
                autoit.send("{up}")
            autoit.send("{ENTER}")
            autoit.mouse_click("left",441, 691)
            autoit.send("{DOWN}")
            autoit.send("{ENTER}")
            #time.sleep(0.1)
            autoit.mouse_click("left",503, 846)
            autoit.win_wait_active("OpenVPN Connect")
            autoit.opt("MouseCoordMode",0)
            autoit.mouse_click("left",140, 401)
            #time.sleep(0.1)
            autoit.mouse_click("left",45, 272)
            
            #time.sleep(0.1)
            autoit.send("a364718")
            #time.sleep(0.1)
            autoit.mouse_click("left",30, 316)
            #time.sleep(0.1)
            autoit.send("{TAB}")
            #time.sleep(0.1)
            autoit.send("2frfvrfzPJ")
            #time.sleep(0.1)
            autoit.mouse_click("left",285, 638)
            #time.sleep(0.1)
            autoit.mouse_click("left",48, 368)
            #time.sleep(0.1)
            autoit.mouse_click("left",308, 426)
            color = 0
            #time.sleep(25)
            autoit.win_activate("Google - Google Chrome")
            autoit.win_wait_active("Google - Google Chrome")
    bar.finish()
        '''
