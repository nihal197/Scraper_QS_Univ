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
    
#TO GET THIS SPECIFIC XPATH WE HAVE TO SCROLL AS WELL AS hover_over TO ACTIVATE IT
scroll = browser.find_element_by_xpath('//*[@id="qs-rankings_length"]/label/span[2]/span[2]')
hover_over(scroll)
scroll_fun(2000)

#GET ALL THE RESULTS IN A SINGLE PAGE
scr_all_menu=browser.find_element_by_xpath('//*[@id="qs-rankings_length"]/label/span[2]/span[2]')
hover_over(scr_all_menu)

lag=browser.find_element_by_xpath('//*[@id="qs-rankings_length"]/label/span[2]/span[2]')
hover_over(lag)

scr_all_menu.click()

#SELECTING ALL FROM DROP DOWN MENU
scr_all=browser.find_element_by_xpath('//*[@id="qs-rankings_length"]/label/span[2]/div/div/span/span/ul/li[5]/span')
hover_over(scr_all)
scr_all.click()

#SCROLLING BACK TO UP TO FETCH THE REGION WISE RESULT
scroll_fun(500)

#SEACHING THE UNI BY NAME
uni_name=input('Enter university name: ')
uni_search_by_name(uni_name)

#GET THE UNIVERSITIES
uni= get_uni()

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

