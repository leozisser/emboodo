import pandas as pd
import random
import re
'''this script works with the sheet of datasets. 
it extracts the information and creates a column with custom dataset description 
based on a template and the information in the columns'''


# filepath = '//Users/leo_z/Downloads/Scraping-data-europe - Construction industry Datasets.csv'
# fp2 = 'lol.csv'
# filepath_alldata = 'construction with location.csv'
# '$vendor_name\'s $(Xplanung|INSPIRE) dataset in the area of $datacat.lower() that can be used in the sphere of use_cases.rfind(',').insert('and')'

def searchreg(el):
    try:
        n = re.search(r'([Tt]own|[cC]ity|[Mm]unicipality)(.+?)(in Xpla|from XP|based on|transforme)',el).group(1,2)
        k = ''.join(list(n))
        return(k.strip(' ').strip(','))
    except:
        return ''


def insert_last_and(st):
    items = st.split(',')
    if len(items)>1:
        return ', '.join(items[:-1]) + ' and '+items[-1]
    else:
        return ', '.join(items)


def jo(st): #not used currently, same as insert_last_and
    st = st.replace(',',', ')
    k = st.rfind(", ")
    new_string = st[:k] + " and" + st[k+1:]
    return new_string


def delete_name(df): #returns df with new column where data vendor name is deleted from dataset name
    # df = pd.read_csv(path).fillna('')
    df['replaced'] = ''
    for i,row in df.iterrows():
        row['replaced'] = row['post_title'].replace(row['data_provider'],'').strip('\'s').strip(': ').strip(' - ').strip(' | ')
    return df


def extract_location_form_description(path): #creates 
    df = pd.read_csv(path).fillna('')
    df = delete_name(df)
    print(df.columns)
    dataname = df['post_title']
    vendor_name = df['data_provider']
    datacat = df['data_category']
    usecases = df['use_case']
    dataname_replaced = df['replaced']
    df['Description_new'] = vendor_name + '\'s dataset - \'' + dataname_replaced + '\' provides '+ datacat.apply(insert_last_and) +' that can be used in '+ usecases.apply(insert_last_and)# + ' in the '+location
    df = df.drop('replaced',axis=1)
    df = df.drop([c for c in df.columns if 'Unnamed' in c],axis=1)
    # df.to_csv('df with description-2.csv', index=False)
    return df



# delete_name('df with description-2.csv')
extract_location_form_description(fp2)

