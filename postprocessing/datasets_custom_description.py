import pandas as pd
import random
import re
import os
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


def add_location(df): #reconstructed; not tested
    df['location'] = df['post_title'].apply(searchreg)
    return df


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


def add_deleted_name(df): #returns df with new column where data vendor name is deleted from dataset name
    # df = pd.read_csv(path).fillna('')
    df['replaced'] = ''
    for i,row in df.iterrows():
        row['replaced'] = row['Name of the dataset'].replace(row['Data Vendor Name'],'').strip('\'s').strip(': ').strip(' - ').strip(' | ')
    return df


def cond(a):
    # print(a)
    # print((len(a)>0)**2)
    return (len(a)>0)**2


def last(s):
    return s.split('.')[-1].lower()

def replace_api(col):
    return col.str.replace(r'\(API.+\)', '', regex=True)


def form_description(df): #creates a description based on a template in a separate column, removes 'unnamed:' columns
    # df = pd.read_csv(path).fillna('')
    df = df.fillna('')
    df = df.astype(str)
    df = add_deleted_name(df)
    print(df.columns)
    descr = df['Description']
    df['Last Sentence'] = descr.apply(last)
    ls = df['Last Sentence']
    dataname = df['Name of the dataset']
    vendor_name = df['Data Vendor Name']
    try:
        datacat = df['Data Categories']
    except:
        datacat = df['Data Category']
    try:
        usecases = df['Use Cases']
    except:
        usecases = df['Use cases']
    dataname_replaced = replace_api(df['replaced']).apply(lambda x:x.strip(' ').strip('.'))
    # dataname_replaced = dataname_replaced.str.replace(r'\(API.+\)', '', regex=True)
    df['Description_new'] = vendor_name + '\'s dataset - \'' + dataname_replaced + '\' ' +( 'provides '+ datacat.apply(insert_last_and))*datacat.apply(cond) + (' that can be used in ' + usecases.apply(insert_last_and))*usecases.apply(cond) + '.'# + ' based on ' + ls + '.' #+  'in the '+location
    df = df.drop('replaced',axis=1)
    df = df.drop([c for c in df.columns if 'Unnamed' in c],axis=1)
    # df.to_csv('df with description-2.csv', index=False)
    return df


if __name__ == '__main__':
    folder_dir = 'dataset_sheets/pipeline/ready'
    result_dir = 'results/pipeline/ready'
    for i in os.listdir(folder_dir):
        print(i)
        df = pd.read_excel(os.path.join(folder_dir,i))
        # print(len([i for i in os.listdir(folder_dir)]))
        # print(df.head())
        dff = form_description(df)
        dff.to_csv(os.path.join(result_dir,i))
    # filepath = '//Users/leo_z/Downloads/Scraping-data-europe - Construction industry Datasets.csv'
    # fp2 = 'lol.csv'
    # filepath_alldata = 'construction with location.csv'
    # delete_name('df with description-2.csv')
    # form_description(fp2)

