# Import Necessary library/drivers
import pandas as pd
import sys, time
from datetime import date, datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Open Chrome Browser
browser = webdriver.Chrome(executable_path=r'C:\Users\User\AppData\Local\Programs\Python\Python39\chromedriver.exe')

# Set Message
msg = "My message 1"

# Navigate whatsapp web
browser.get('https://web.whatsapp.com/')
time.sleep(5)

# Get numbers from Excel Sheet
whatsapp_number_sheet = pd.read_excel('whatsapp_number_sheet.xlsx')

#get search box of whatsapp web
search_bar = browser.find_element_by_xpath('//div[@class="_13NKt copyable-text selectable-text"]')

#Get number from excel sheet and search
number = str(whatsapp_number_sheet['Whatsapp'].tolist()[0])
search_query = "+880 "+str(number[0:4])+"-"+str(number[4:10])
search_bar.send_keys(search_query)
time.sleep(10)

# Select User
user = browser.find_element_by_xpath('//span[@title="{}"]'.format(search_query))
user.click()

time.sleep(2)
message = browser.find_element_by_xpath('//div[@class="p3_M1"]')
time.sleep(2)

message.send_keys(msg)
time.sleep(6)

send_button = browser.find_element_by_xpath('//div[@class="_3HQNh _1Ae7k"]/button').click()

data_to_be_written = pd.DataFrame({'Whatsapp':["0"+str(whatsapp_number_sheet['Whatsapp'].tolist()[0])], 'Status':['sent']})

data_to_be_written.to_excel('./whatsapp_number_sheet.xlsx')