from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
from google.oauth2.service_account import Credentials
url='https://www.linkedin.com/login?'
driver = webdriver.Chrome("./chromedriver")
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
username = driver.find_element_by_id("username")

# send_keys() to simulate key strokes
username.send_keys('m.naufil1@gmail.com')
password = driver.find_element_by_id("password")
password.send_keys('1schoollife@')
log_in_button = driver.find_element_by_class_name('login__form_action_container')

# .click() to mimic button click
log_in_button.click()
# phone_name = soup.find_all('div', {"class":"_2lebQ1R-ufCP5dNpJUTtep"})
# price_per_month = soup.find_all('div', {'class':'_3Cpr5ktg8eh2LI40eTZOYy'}) # price per month
# interest = soup.find_all('div', {'class':'_19KqXVLwnv4Tdrl6Z5Caw4 _3skKfvMN7NMmiM_zTRFUde _2WLZkEZQFh-vi4QmWFOLG_'}) # interest
# total_price = soup.find_all('div', {'class':'_1FykWgSNzyIy5hEGsGhj33'}) # total_price
# unlimited_offer = soup.find_all('div', {'class':'_1lqQj4dE_WnGwWg3KfbDLU'})

# phone_name_list=[]
# price_per_month_list=[]
# interest_list=[]
# total_price_list=[]
# unlimited_offer_list=[]

# for phone in phone_name:
#     phone_name_list.append(phone.text)
# for price in price_per_month:
#     price_per_month_list.append(price.text)
# for interes in interest:
#     interest_list.append(interes.text)
# for total in total_price:
#     total_price_list.append(total.text)
# for offer in unlimited_offer:
#     unlimited_offer_list.append(offer.text)
# s1 = pd.Series(phone_name_list, name='Phone Name')
# s2 = pd.Series(price_per_month_list, name='Price Per Month')
# s3 = pd.Series(interest_list, name='Interest')
# s4 = pd.Series(total_price_list, name='Total Price')
# s5 = pd.Series(unlimited_offer_list, name='Unlimited Offer')
# df = pd.concat([s1,s2,s3,s4,s5], axis=1)
# df = df.fillna("None")
# # d = {'Phone name': phone_name_list, 'Price per month': price_per_month_list,'Interest List': interest_list, 'Total Price List': total_price_list,'Unlimited Offer List': unlimited_offer_list}
# # df = pd.DataFrame(data=d)
# print(df)
# df.to_csv('naufil.csv', encoding='utf-8')
# scope = ['https://spreadsheets.google.com/feeds',
#          'https://www.googleapis.com/auth/drive']
# credentials = Credentials.from_service_account_file('scrapper-phones-8279178067ae.json', scopes=scope)
# gc = gspread.authorize(credentials)
# spreadsheet_key = '1_f9tc1ylxe8yBna12_ixxq5CYUh15md0tBbD9Jeahqc'
# wks_name = 'Master'
# d2g.upload(df, spreadsheet_key, wks_name, credentials=credentials, row_names=True)
# print(phone_name)
# print(price_per_month)
# print(interest)
# print(total_price)
# print(unlimited_offer)