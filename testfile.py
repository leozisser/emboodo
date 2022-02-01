import re

str1 = 'apples,oranges,lol&bol,foo,bar'
str2 = 'foo'


def join_and(st):
    items = st.split(',')
    if len(items)>1:
        return ', '.join(items[:-1]) + ' and '+items[-1]
    else:
        return ', '.join(items)



def jo(st):
    st = st.replace(',',', ')
    k = st.rfind(", ")
    new_string = st[:k] + " and " + st[k+1:]
    return new_string

def insert_last_and(st):
    return join_and(st.split(','))

print(jo(str1))

