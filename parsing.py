from bs4 import BeautifulSoup
import requests
from time import sleep
n = 0
while n < 100:
    n += 1
    url = "https://jut.su/anime/"# url страницы
    r = requests.get(url)
    with open('test.html', 'w') as output_file:
      output_file.write(r.text)
    sleep(1)
    print(0)
