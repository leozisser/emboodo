from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import autoit
import random
import time

first_names = ["Samuel","Jack","Joseph","Harry","Alfie","Jacob","Thomas","Charlie","Oscar","James","William","Joshua","George","Ethan","Noah","Archie","Henry","Leo","John","Oliver","David","Ryan","Dexter","Connor","Albert","Austin","Stanley","Theodore","Owen","Caleb"]
family_names = ["Williams","Peters","Gibson","Martin","Jordan","Jackson","Grant","Davis","Collins","Bradley","Barlow"]

# Instantiate Chrome Browser Command
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
# Open the provided URL
driver.get("https://staging.app.timelines.ai/accounts/login/?next=/")
#elem = driver.find_element_by_name("email")
#elem.send_keys("")
driver.find_element_by_class_name("btn-primary").click()
new_page = driver.find_element_by_tag_name('html')
first_name = driver.find_element_by_id("id_first_name")
number = random.randint(0,len(first_names))
first_name.send_keys(first_names[number])
family_name = driver.find_element_by_id("id_last_name")
number = random.randint(0,len(family_names) -1)
family_name.send_keys(family_names[number])
company_name = driver.find_element_by_id("id_display_name")
company_name.send_keys("masatlalim")
email = driver.find_element_by_name("email")
randnum = time.strftime("%j%m%M%S")
email.send_keys("danil.ershov" + str(randnum) + "@initech.co.il")
driver.find_element_by_id('select2-id_timezone-container').click()
timezonename = (driver.find_element_by_class_name('select2-search__field'))
timezonename.send_keys("Moscow")
driver.implicitly_wait(10)
driver.find_element_by_class_name('select2-results').click()

password = driver.find_element_by_name("password")
password.send_keys("123456789Mm")
password = driver.find_element_by_name("password_repeat")
password.send_keys("123456789Mm")

driver.find_element_by_id('id_accepted_conditions').click()






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
# import autoit
import random
import time

first_names = ["Samuel","Jack","Joseph","Harry","Alfie","Jacob","Thomas","Charlie","Oscar","James","William","Joshua","George","Ethan","Noah","Archie","Henry","Leo","John","Oliver","David","Ryan","Dexter","Connor","Albert","Austin","Stanley","Theodore","Owen","Caleb"]
family_names = ["Williams","Peters","Gibson","Martin","Jordan","Jackson","Grant","Davis","Collins","Bradley","Barlow"]

# Instantiate Chrome Browser Command
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
# Open the provided URL
driver.get("https://staging.app.timelines.ai/accounts/login/?next=/")
#elem = driver.find_element_by_name("email")
#elem.send_keys("")
driver.find_element_by_class_name("btn-primary").click()
new_page = driver.find_element_by_tag_name('html')
first_name = driver.find_element_by_id("id_first_name")
number = random.randint(0,len(first_names))
first_name.send_keys(first_names[number])
family_name = driver.find_element_by_id("id_last_name")
number = random.randint(0,len(family_names) -1)
family_name.send_keys(family_names[number])
company_name = driver.find_element_by_id("id_display_name")
company_name.send_keys("masatlalim")
email = driver.find_element_by_name("email")
randnum = time.strftime("%j%m%M%S")
email.send_keys("danil.ershov" + str(randnum) + "@initech.co.il")
driver.find_element_by_id('select2-id_timezone-container').click()
timezonename = (driver.find_element_by_class_name('select2-search__field'))
timezonename.send_keys("Moscow")
driver.implicitly_wait(10)
driver.find_element_by_class_name('select2-results').click()

password = driver.find_element_by_name("password")
password.send_keys("123456789Mm")
password = driver.find_element_by_name("password_repeat")
password.send_keys("123456789Mm")

driver.find_element_by_id('id_accepted_conditions').click()
#driver.find_element_by_class_name('recaptcha-checkbox-border').click()

autoit.opt("MouseCoordMode",0)
autoit.mouse_click("left",305, 936)
autoit.mouse_move(0,0)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
# import autoit
import random

import time
def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except Exception:
        return False
    return True
first_names = ["Samuel","Jack","Joseph","Harry","Alfie","Jacob","Thomas","Charlie","Oscar","James","William","Joshua","George","Ethan","Noah","Archie","Henry","Leo","John","Oliver","David","Ryan","Dexter","Connor","Albert","Austin","Stanley","Theodore","Owen","Caleb"]
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.get("https://www.facebook.com/")
#driver.find_element_by_id('u_0_2_7y').click()
driver.find_element('xpath','/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a').click()
while not check_exists_by_xpath(driver,'/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input'):
    pass
driver.find_element('xpath','/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input').send_keys('123')
number=random.randint(0,len(first_names))
number.send_keys(first_names[number])
driver.find_element('xpath','/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input').send_keys(tel_number)

















