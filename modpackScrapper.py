from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def get_downloads(str):
    return int(str.split('|')[2].split(' ')[1].replace(',',''))

try:
    df = pd.read_csv('modpacks.csv')
    df.drop_duplicates(inplace=True)
except:
    b = webdriver.Chrome()
    df = pd.DataFrame()
    b.get('https://www.modpackindex.com/mod/7740/gregtech-community-edition')
    time.sleep(2)
    for _ in range(30):
        time.sleep(2)
        df = df.append(pd.read_html(b.page_source)[0])
        b.find_element(By.ID,'modpacks-table_next').click()
    df.to_csv('modpacks.csv')
finally:
    modpacks = {}
    modpacks = df['Name & Summary'].apply(get_downloads).to_dict()
    sorted_modpacks = dict(sorted(modpacks.items(), key=lambda item: item[1]))
    print(df.iloc[list(sorted_modpacks.keys())[-30:]])