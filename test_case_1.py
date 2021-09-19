# Import Necessary library/drivers
import pandas as pd
import sys, time
from datetime import date, datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Open Chrome Browser
browser = webdriver.Chrome(executable_path=r'C:\Users\User\AppData\Local\Programs\Python\Python39\chromedriver.exe')

# Navigate whatsapp web
browser.get('https://web.whatsapp.com/')
time.sleep(5)

# Get numbers from Excel Sheet
whatsapp_number_sheet = pd.read_excel('whatsapp_number_sheet.xlsx')

#get search box of whatsapp web
search_bar = browser.find_element_by_xpath('//div[@class="_13NKt copyable-text selectable-text"]')

#Get number from excel sheet and search
search_bar.send_keys("0"+str(whatsapp_number_sheet['Whatsapp'].tolist()[0]))