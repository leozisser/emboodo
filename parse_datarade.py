import requests
# from fake_useragent import UserAgent
# import selenium
# import bs4 as bs

url = 'https://datarade.ai/data-providers/acxiom/profile'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response.content)
