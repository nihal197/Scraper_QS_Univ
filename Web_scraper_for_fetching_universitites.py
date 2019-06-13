#IMPORTING RELEVENT LIBRARIES

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
from utils import *
import warnings
warnings.filterwarnings('ignore')

#INITLIAZE A BROWSER
browser= webdriver.Chrome('C:\Selenium\chromedriver', chrome_options=options)

#URL OF QS-WORLD RANKINGS 2019
url=r'https://www.topuniversities.com/university-rankings/world-university-rankings/2019'
browser.get(url)
    
#TO GET THIS SPECIFIC XPATH WE HAVE TO SCROLL AS WELL AS HOVER TO ACTIVATE IT
scroll = browser.find_element_by_xpath('//*[@id="qs-rankings_length"]/label/span[2]/span[2]')
hover(scroll)
browser.execute_script("window.scrollTo(0,2000)") 

#GET ALL THE RESULTS IN A SINGLE PAGE
scr_all_menu=browser.find_element_by_xpath('//*[@id="qs-rankings_length"]/label/span[2]/span[2]')
hover(scr_all_menu)

lag=browser.find_element_by_xpath('//*[@id="qs-rankings_length"]/label/span[2]/span[2]')
hover(lag)

scr_all_menu.click()

#SELECTING ALL FROM DROP DOWN MENU
scr_all=browser.find_element_by_xpath('//*[@id="qs-rankings_length"]/label/span[2]/div/div/span/span/ul/li[5]/span')
hover(scr_all)
scr_all.click()

#SCROLLING BACK TO UP TO FETCH THE REGION WISE RESULT
browser.execute_script("window.scrollTo(0,500)") 

#DROP DOWN MENU FOR SELECTING REGION 
drop=browser.find_element_by_xpath('//*[@id="qs-rankings"]/thead/tr[3]/td[3]/div/div/span[2]/span[2]')
hover(drop)
drop.click() 

#PRINTING LIST OF ITEMS IN THE DROP DOWN MENU
region_list=browser.find_elements_by_class_name('jcf-option')
sel_print_region(region_list)

#INPUT REGION
region=input('Input the region: ')
input_region(region)

#Standard Function for search

# def uni_search_by_name(uni_name):
#     uni_search=browser.find_element_by_xpath('//*[@id="qs-rankings"]/thead/tr[3]/td[2]/div/input')
#     uni_name=input('Enter_uni_name: ')
#     uni_search.send_keys(uni_name)
#     #Range of other functions doing their stuff here
    

#LIST OF ALL UNIVERSITIES
uni= get_uni()

#RANKS OF ALL THE UNIVERSITIES
rank = get_rank()

#FINDING THE COUNTRY 
ctry = get_country()

#RETURNING A DATAFRAME WITH ALL THE THREE COLUMNS
uni_data(ctry,rank,uni)

#GET THE NAME OF THE UNIVERSITY SELECTED AS WELL AS CLICKING THE PAGE FOR MORE INFO
#SELECT ANY INDEX FROM THE DATAFRAME
index=input("Enter the index of the university you want to know more about: ")

uni_info(index)

#COMBINING LOCATION RELEVENT DETAILS OF THE UNIVERSITY TO FORM A DATAFRAME 
df=com_details()

#TO FETCH THE OVERVIEW OF THE UNIVERSITY SELECTED
#INSERTING THE PARAGRAPH
df['Overview']=fetch_para()

#SINCE THE WEBSITE DOES NOT PROVIDE THE LINK TO THE UNIVERSITY WE GOOGLE THE TOPMOST RESULT
df['Link']=google_the_link(uni_info.uni_name)

#INSERTING THE DATA INTO OUR DATAFRAME 
df['Name']=uni_info.uni_name
df.set_index('Name',inplace=True)

#SAVING THE FILE WITH UNIVERSITY NAME 
df.to_csv(uni_info.uni_name+str('.csv'))

