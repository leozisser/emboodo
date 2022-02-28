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

import autoit
import random
import time
LOGGER.setLevel(logging.WARNING)
'''
start_time = time.time()
for a in range(0,265):
    for b in range(0,265):
        for c in range(0,265):
            #print("--- %s seconds ---" % (time.time() - start_time))
            for d in range(0,265):
                #print("--- %s seconds ---" % (time.time() - start_time))
                for e in range(0,265):
                    #print(str(a)+"."+str(b)+"."+str(c)+"."+str(d)+":"+str(e))
                    pass

'''
options = Options()
#options.add_argument('--proxy-server=176.9.119.170:1080	')
options.add_argument("no-sandbox")
options.add_argument("--disable-gpu")
#options.add_argument("--window-size=1200,1200")
options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--headless")
#options.add_argument("--host-resolver-rules=MAP www.google-analytics.com 127.0.0.1")
options.add_argument("no-default-browser-check")
options.add_argument("no-first-run")
def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element("xpath",xpath)
    except Exception:
        return False
    return True
first_names = ["Samuel","Jack","Joseph","Harry","Alfie","Jacob","Thomas","Charlie","Oscar","James","William","Joshua","George","Ethan","Noah","Archie","Henry","Leo","John","Oliver","David","Ryan","Dexter","Connor","Albert","Austin","Stanley","Theodore","Owen","Caleb"]
family_names = ["Williams","Peters","Gibson","Martin","Jordan","Jackson","Grant","Davis","Collins","Bradley","Barlow"]
month = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
coords = ["183","298","413","528","643","758","873"]
autoit.opt("MouseCoordMode",0)
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=options
)
coords_number = 0
# Open the provided URL
driver.get("https://datarade.ai/data-categories")
driver.maximize_window()

    
c = driver.find_elements(By.CLASS_NAME,"sub-category__row")
'''
for b in range(1,len(c)):
    a = driver.find_element("xpath","/html/body/div[1]/main/div/div[2]/div/div/div/article[1]/div[2]/div["+ str(b) +"]/div[1]/a").text
    #print(a)

'''
v = 0
b = 1
g = 1
try1 = 0
href_list_0_level = []
href_list_1_level = []
href_list_2_level = []
href_list_3_level = []
vpn_number = 1
##print(len(c))
while try1 < 10:
    for f in range(0,2):
        a = check_exists_by_xpath(driver,"/html/body/div[1]/main/div/div[2]/div/div/div/article["+str(g)+"]/div[2]/div["+ str(b) +"]/div[1]/a")
        ##print(b)
        ##print(a)
    ##print(a)
    if a == True:
        try1 = 0
        elem = driver.find_element("xpath","/html/body/div[1]/main/div/div[2]/div/div/div/article["+str(g)+"]/div[2]/div["+ str(b) +"]/div[1]/a")
        m = driver.find_element("xpath","/html/body/div[1]/main/div/div[2]/div/div/div/article["+str(g)+"]/div[2]/div["+ str(b) +"]/div[1]/a").text
        href_list_0_level.append( elem.get_attribute('href'))
        b +=1
        
        ##print(m)
        
    else:
        b = 1
        g += 1
        try1 += 1
        #m = driver.find_element("xpath","/html/body/div[1]/main/div/div[2]/div/div/div/article["+str(g)+"]/div[2]/div["+ str(b) +"]/div[1]/a").text
    ##print(v,len(c))
    
    ##print(b)
##print(href)
href_list = []
datasets_href_list = []
text_of_ban = ""
f = open(r'C:\Users\Анатолий\Desktop\python\scraping.txt', 'w')
q = 0
while q < len(href_list_0_level):
    
    elem_1 = ""
    list_checked = []
    href_list_1_level = []
    href_list_2_level = []
    href_list_3_level = []
    depth = 2
    #print(a)
    driver.execute_script("window.open("+"'"+href_list_0_level[q]+"'"+");")
    driver.switch_to.window(driver.window_handles[1])
    text_of_ban = driver.find_element("xpath","/html/body")
    print(text_of_ban.text[0:20])
    if text_of_ban.text !="Too many requests in a given amount of time. We employ rate limiting to ensure the stability of our services to all users. If you think this is a mistake, contact us at platform@datarade.ai":
        q+= 1
    
        #time.sleep(0.1)
        
        #time.sleep(0.1)
        amount = driver.find_element("xpath","/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[2]/div[1]/div/div")
        amount = amount.text
        if len(amount) > 15:
            number = 3
            #print("pass")
        else:
            number = 0
        if number == 3:
            for qwerty in range(1,len(handles_list)):
                time.sleep(0.1)
                autoit.send("^w")
                time.sleep(0.1)
            driver.switch_to.window(driver.window_handles[0])
        elif number == 0:
            for j in range(1,3):
                checksum_lvl_1 = check_exists_by_xpath(driver,"/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(j)+"]")
                #time.sleep(0.1)
                checksum_lvl_1 = check_exists_by_xpath(driver,"/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(j)+"]")

                #/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/div
                #/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a[12]
                #/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/div
                #/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a[7]
                #/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav
                #print(checksum_lvl_1)
                #print("/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(j)+"]")
                if checksum_lvl_1 == True :
                    elem = driver.find_element("xpath","/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(j)+"]")
                    class_name = elem.get_attribute("class")
                    elem = driver.find_element_by_xpath("//*")
                    source_code = elem.get_attribute("outerHTML")
                    number_2 = source_code.find("tree-nav__node tree-nav__node--depth-"+str(depth)+" tree-nav__node--interesting")
                    first_nav_number = source_code.rfind("<nav",0,number_2)
                    source_code = source_code[first_nav_number:]
                    number_2 = source_code.find("nav>")
                    source_code = source_code[:number_2]
                    list = source_code.split("><")
                    list = list[1:-1]
                    #print()
                    #print("tree-nav__node tree-nav__node--depth-"+str(depth)+" tree-nav__node--interesting")
                    for i in list:
                        if i.find("tree-nav__node tree-nav__node--depth-"+str(depth)+" tree-nav__node--interesting") != -1:
                            if i in list_checked:
                                pass
                            else:
                                list_checked.append(i)
                            href_list_1_level
            for i in list_checked:
                a = i.split('"/')
                a = a[1][:-3]
                a = a.split('">')
                a = a[0]
                #print("/"+a)
                href_list_1_level.append("/"+a)
                    #print(elem_1)
                        
                        
            if href_list_1_level != []:
                #print(123)
                #print(href_list_1_level)
                #time.sleep(0.1)
                depth += 1
                hreflist1 = 0
                while hreflist1 < len(href_list_1_level):
                    #print(i)
                    driver.execute_script("window.open("+"'"+str(href_list_1_level[hreflist1])+"'"+");")
                    lkj = 0
                    while lkj <3:
                        driver.switch_to.window(driver.window_handles[lkj])
                        #print(driver.current_url)
                        if driver.current_url.find(href_list_1_level[hreflist1]) == "-1":
                            pass
                            lkj += 1
                        else:
                            lkj = 5
                    text_of_ban = driver.find_element("xpath","/html/body")
                    print(text_of_ban.text[0:20])
                    if text_of_ban.text !="Too many requests in a given amount of time. We employ rate limiting to ensure the stability of our services to all users. If you think this is a mistake, contact us at platform@datarade.ai":
                        
                        #time.sleep(0.1)
                        
                        hreflist1 += 1
                        for p in range(1,30):
                            checksum_lvl_2 = check_exists_by_xpath(driver,"/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(p)+"]")
                            #time.sleep(0.1)
                            checksum_lvl_2 = check_exists_by_xpath(driver,"/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(p)+"]")
                            #print(checksum_lvl_2)
                            #print("/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(p)+"]")
                            if checksum_lvl_2 == True :
                                elem = driver.find_element("xpath","/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(p)+"]")
                                class_name = elem.get_attribute("class")
                                elem = driver.find_element_by_xpath("//*")
                                source_code = elem.get_attribute("outerHTML")
                                number_2 = source_code.find("tree-nav__node tree-nav__node--depth-"+str(depth)+" tree-nav__node--interesting")
                                first_nav_number = source_code.rfind("<nav",0,number_2)
                                source_code = source_code[first_nav_number:]
                                number_2 = source_code.find("nav>")
                                source_code = source_code[:number_2]
                                list = source_code.split("><")
                                list = list[1:-1]
                                #print()
                                #print("tree-nav__node tree-nav__node--depth-"+str(depth)+" tree-nav__node--interesting")
                                for i in list:
                                    if i.find("tree-nav__node tree-nav__node--depth-"+str(depth)+" tree-nav__node--interesting") != -1:
                                        a = i.split('"/')
                                        a = a[1][:-3]
                                        a = a.split('">')
                                        a = a[0]
                                        #print("/"+a)
                                #print(elem_1)
                                href_list_2_level = []
                                if class_name == "tree-nav__node tree-nav__node--depth-"+str(depth)+" tree-nav__node--interesting":
                                    
                                    href_list_2_level.append("/"+a)
                        if href_list_2_level != []:
                            depth += 1
                            #print(123)
                            #print(href_list_2_level)
                            f = 0
                            while f < len(href_list_2_level):
                                driver.execute_script("window.open("+"'"+str(f)+"'"+");")
                                lkj = 0
                                while lkj <len(driver.window_handles):
                                    driver.switch_to.window(driver.window_handles[lkj])
                                    #print(driver.current_url)
                                    if driver.current_url.find(href_list_2_level[f]) == "-1":
                                        pass
                                        lkj += 1
                                    else:
                                        lkj = 5
                                text_of_ban = driver.find_element("xpath","/html/body")
                                print(text_of_ban.text[0:20])
                                if text_of_ban.text !="Too many requests in a given amount of time. We employ rate limiting to ensure the stability of our services to all users. If you think this is a mistake, contact us at platform@datarade.ai":
                                    #time.sleep(0.1)
                                    f += 1
                                    
                                    href_list_3_level = []
                                    for d in range(1,30):
                                        checksum_lvl_3 = check_exists_by_xpath(driver,"/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(d)+"]")
                                        #time.sleep(0.1)
                                        checksum_lvl_3 = check_exists_by_xpath(driver,"/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(d)+"]")

                                        #driver.find_element("xpath","/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(d)+"]")
                                        #print(checksum_lvl_3)
                                        #print("/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(d)+"]")
                                        if checksum_lvl_3 == True :
                                            elem = driver.find_element("xpath","/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[1]/nav/a["+str(d)+"]")
                                            class_name = elem.get_attribute("class")
                                            elem = driver.find_element_by_xpath("//*")
                                            source_code = elem.get_attribute("outerHTML")
                                            number_2 = source_code.find("tree-nav__node tree-nav__node--depth-"+str(depth)+" tree-nav__node--interesting")
                                            first_nav_number = source_code.rfind("<nav",0,number_2)
                                            source_code = source_code[first_nav_number:]
                                            number_2 = source_code.find("nav>")
                                            source_code = source_code[:number_2]
                                            list = source_code.split("><")
                                            list = list[1:-1]
                                            
                                            #print()
                                            #print("tree-nav__node tree-nav__node--depth-"+str(depth)+" tree-nav__node--interesting")
                                            for mmm in list:
                                                if mmm.find("tree-nav__node tree-nav__node--depth-"+str(depth)+" tree-nav__node--interesting") != -1:
                                                    a = mmm.split('"/')
                                                    a = a[1][:-3]
                                                    a = a.split('">')
                                                    a = a[0]
                                                    #print("/"+a)
                                            #print(elem_1)
                                            href_list_3_level = []
                                            if class_name == "tree-nav__node tree-nav__node--depth-"+str(depth)+" tree-nav__node--interesting":
                                                
                                                href_list_3_level.append("/"+a)
                                    if href_list_3_level != []:
                                        #print("3rd level")
                                        pass
                                    else: 
                                        datasets_list = driver.find_elements(By.CLASS_NAME,"data-product-card__title ")
                                        #print(datasets_list)
                                        #print(432)
                                        f = open(r'C:\Users\Анатолий\Desktop\python\scraping.txt', 'a')
                                        for qwerty in range(1,len(datasets_list) + 1):
                                            checking = check_exists_by_xpath(driver,"/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[2]/div[2]/article["+str(qwerty)+"]/main/div[2]/a")
                                            if checking == True:
                                                dataset_href = driver.find_element("xpath","/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[2]/div[2]/article["+str(qwerty)+"]/main/div[2]/a").get_attribute('href')
                                                print(dataset_href)
                                                datasets_href_list.append(dataset_href)
                                                
                                                f.write(dataset_href + "\n")
                                                
                                            else:
                                                pass
                                        f.close()
                                            #/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[2]/div[2]/article[1]/main/div[2]/a
                                            #/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[2]/div[2]/article[1]/main/div[2]/a
                                        handles_list = driver.window_handles
                                        for qwerty1 in range(1,len(handles_list)):
                                            time.sleep(0.1)
                                            autoit.send("^w")
                                            time.sleep(0.1)
                                        driver.switch_to.window(driver.window_handles[0])
                                        #time.sleep(0.1)
                                else:
                                    time.sleep(0.1)
                                    #driver.execute_script("window.open('https://www.google.com/')")
                                    handles_list = driver.window_handles
                                    qwerty = len(handles_list)
                                    qwerty -=1
                                    while qwerty >=0:
                                        driver.switch_to.window(driver.window_handles[qwerty])
                                        text_of_ban = driver.find_element("xpath","/html/body")
                                        print(text_of_ban.text[0:20])
                                        if text_of_ban.text =="Too many requests in a given amount of time. We employ rate limiting to ensure the stability of our services to all users. If you think this is a mistake, contact us at platform@datarade.ai":
                                            autoit.send("^w")
                                            time.sleep(0.1)
                                        qwerty -= 1
                                    else:
                                        pass
                                    driver.switch_to.window(driver.window_handles[0])
                                    autoit.win_activate("OpenVPN Connect")
                                    autoit.win_wait_active("OpenVPN Connect")
                                    autoit.mouse_click("left",60, 183)
                                    time.sleep(10)
                                    autoit.mouse_click("left",37, int(coords[vpn_number]))
                                    vpn_number+= 1
                                    time.sleep(10)
                        else: 
                            datasets_list = driver.find_elements(By.CLASS_NAME,"data-product-card__title ")
                            #print(datasets_list)
                            #print(213)
                            abc = 1
                            div = 2
                            f = open(r'C:\Users\Анатолий\Desktop\python\scraping.txt', 'a')
                            for i in range(1,len(datasets_list) + 1):
                                checking = check_exists_by_xpath(driver,"/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[2]/div[2]/article["+str(i)+"]/main/div[2]/a")
                                if checking == True:
                                    dataset_href = driver.find_element("xpath","/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[2]/div[2]/article["+str(i)+"]/main/div[2]/a").get_attribute('href')
                                    print(dataset_href)
                                    datasets_href_list.append(dataset_href)
                                    
                                    f.write(dataset_href + "\n")
                            
                                else:
                                    pass
                            f.close()
                            handles_list = driver.window_handles
                            for qwerty in range(1,len(handles_list)):
                                time.sleep(0.1)
                                autoit.send("^w")
                                time.sleep(0.1)
                            driver.switch_to.window(driver.window_handles[0])
                            
                    else:
                        qwerty = 0
                        time.sleep(0.1)
                        #driver.execute_script("window.open('https://www.google.com/')")
                        handles_list = driver.window_handles
                        qwerty = len(handles_list)
                        qwerty -=1
                        while qwerty >=0:
                            driver.switch_to.window(driver.window_handles[qwerty])
                            text_of_ban = driver.find_element("xpath","/html/body")
                            print(text_of_ban.text[0:20])
                            if text_of_ban.text =="Too many requests in a given amount of time. We employ rate limiting to ensure the stability of our services to all users. If you think this is a mistake, contact us at platform@datarade.ai":
                                autoit.send("^w")
                                time.sleep(0.1)
                            qwerty -= 1
                        else:
                            pass
                        driver.switch_to.window(driver.window_handles[0])
                        autoit.win_activate("OpenVPN Connect")
                        autoit.win_wait_active("OpenVPN Connect")
                        autoit.mouse_click("left",60, 183)
                        time.sleep(10)
                        autoit.mouse_click("left",37, int(coords[vpn_number]))
                        vpn_number+= 1
                        time.sleep(10)
                                        
            else: 
                datasets_list = driver.find_elements(By.CLASS_NAME,"data-product-card__title ")
                #print(datasets_list)
                #print(123)
                f = open(r'C:\Users\Анатолий\Desktop\python\scraping.txt', 'a')
                for i in range(1,len(datasets_list) + 1):
                    checking = check_exists_by_xpath(driver,"/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[2]/div[2]/article["+str(i)+"]/main/div[2]/a")
                    if checking == True:
                        dataset_href = driver.find_element("xpath","/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[2]/div[2]/article["+str(i)+"]/main/div[2]/a").get_attribute('href')
                        print(dataset_href)
                        datasets_href_list.append(dataset_href)
                        
                        f.write(dataset_href + "\n")
                        
                    else:
                        pass
                f.close()
                handles_list = driver.window_handles
                for qwerty in range(1,len(handles_list)):
                    time.sleep(0.1)
                    autoit.send("^w")
                    time.sleep(0.1)
                driver.switch_to.window(driver.window_handles[0])
    else: 
        
        time.sleep(0.1)
        #driver.execute_script("window.open('https://www.google.com/')")
        handles_list = driver.window_handles
        qwerty = len(handles_list)
        qwerty -=1
        while qwerty >=0:
            driver.switch_to.window(driver.window_handles[qwerty])
            text_of_ban = driver.find_element("xpath","/html/body")
            print(text_of_ban.text[0:20])
            if text_of_ban.text =="Too many requests in a given amount of time. We employ rate limiting to ensure the stability of our services to all users. If you think this is a mistake, contact us at platform@datarade.ai":
                autoit.send("^w")
                time.sleep(0.1)
            qwerty -= 1
        else:
            pass
        driver.switch_to.window(driver.window_handles[0])
        autoit.win_activate("OpenVPN Connect")
        autoit.win_wait_active("OpenVPN Connect")
        autoit.mouse_click("left",60, 183)
        time.sleep(10)
        autoit.mouse_click("left",37, int(coords[vpn_number]))
        vpn_number+= 1
        time.sleep(10)
        