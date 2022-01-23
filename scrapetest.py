from bs4 import BeautifulSoup

with open('output1.html','r') as s:
    src = s.read()


def get_list_of_texts_by_class(soup, class_name):    
    datacat = soup.findAll(attrs={"class" : class_name}) 
    return[i.text for i in datacat]


soup = BeautifulSoup(src, features="html.parser")
classname_datacat = "tag-label tag-label--green"
classname_usecase = "tag-label tag-label--blue"
def get_data_cat(soup):
    return get_list_of_texts_by_class(soup,classname_datacat)

def get_usecases(soup):
    return get_list_of_texts_by_class(soup,classname_usecase)

print(get_data_cat(soup))
print(get_usecases(soup))



# selector = 'div > h3 ~ div'
# found = soup.select(selector)
# print(len(found))
# for i in found:
#     print(i)

#     heading = soup.findAll(attrs={"class" : "tag-label tag-label--green")   
#     if heading.text == 'Data Offering':
#         print('1')
# print('0')