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


#INPUT REGION
def input_region(region):
    for i in range(len(a)):
        if i<7 and a[i].text==region:
            print(a[i].text)
            a[i].click()
            break

#HOVER FUNCTION
def hover(element_to_hover_over):
    hover = ActionChains(browser).move_to_element(element_to_hover_over)
    hover.perform()
    
    
#PRINTING THE TEXT 
    def sel_print_region(obj_ls):
        for i in range(6):
            print(obj_ls[i].text)
    
    
#LIST OF ALL UNIVERSITIES
def get_uni():
    get_uni.list_uni=browser.find_elements_by_class_name('title')
    uni=[]
    for i in range(len(get_uni.list_uni)):
        uni.append(get_uni.list_uni[i].text)
    return uni


#RANKS OF ALL THE UNIVERSITIES
def get_rank():
    list_rank=browser.find_elements_by_class_name('rank')
    rank_list=[]
    for i in range(int(len(list_rank)/2)):
        if i>0:
            if list_rank[i*2+1].text!='':
                rank_list.append(list_rank[i*2+1].text)   
            else:
                break
    return rank_list


#FINDING THE COUNTRY 
def get_country():
    list_cntry=browser.find_elements_by_class_name('td-wrap')
    ctry_list=[]
    for i in range(int((len(list_cntry)-15)/5)):
        j=i*5+15+2
        if list_cntry[j].text!='':
            ctry_list.append(list_cntry[j].text)
    return ctry_list


#RETURNING A DATAFRAME WITH ALL THE THREE COLUMNS
def uni_data(ctry,rank,uni):
    df_ctry = pd.DataFrame(ctry,columns=['Country'])
    df_rank = pd.DataFrame(rank,columns=['Rank'])
    df_uni = pd.DataFrame(uni,columns=['University'])
    df=pd.concat([df_rank,df_ctry,df_uni],axis=1)
    return df


#GET THE NAME OF THE UNIVERSITY SELECTED AS WELL AS CLICKING THE PAGE FOR MORE INFO
def uni_info(index):
    uni_info.uni_name=(get_uni.list_uni[index].text)
    print(get_uni.list_uni[index].text)
    ActionChains(browser).move_to_element(get_uni.list_uni[index]).perform()
    get_uni.list_uni[index].click()


#TO FETCH THE OVERVIEW OF THE UNIVERSITY SELECTED
def fetch_para():
    para_str=''
    more = browser.find_elements_by_class_name('more-link')
    if len(more)>0:
        more.click()
        para= browser.find_elements_by_class_name('field-profile-overview')
        list_paras = para[1].find_elements_by_tag_name('p')
        for i in range(len(list_paras)-1):
            para_str+=list_paras[i].text
    else :
        list_paras=browser.find_elements_by_class_name('field-profile-overview')[0].find_elements_by_tag_name('p')
        for i in range(len(list_paras)):
            para_str+=list_paras[i].text
    return para_str


#RELEVENT DETAILS OF THE UNIVERSITY FROM THE SAME PAGE
def details():
    val = browser.find_elements_by_class_name('val')
    lab = browser.find_elements_by_class_name('lab')
    lab_list=[]
    val_list=[]
    for i in range(len(val)-1):
        val_list.append(val[i].text)
        lab_list.append(lab[i].text)
    return pd.DataFrame.from_dict(data=dict(zip(lab_list,val_list)),orient='index').T


#LOCATION OF THE UNIVERSITY 
def location():
    locality = browser.find_element_by_class_name('locality').text
    state = browser.find_element_by_class_name('state').text
    pin = browser.find_element_by_class_name('postal-code').text
    country = browser.find_elements_by_class_name('country')[1].text
    return pd.DataFrame.from_dict({'locality':locality,'State':state,'PIN':pin,"Country":country},orient='index').T


#COMBINING THEM TO FORM A DATAFRAME 
def com_details():
    return pd.concat([details(),location()],axis=1)


#SINCE THE WEBSITE DOES NOT PROVIDE THE LINK TO THE UNIVERSITY WE GOOGLE THE TOPMOST RESULT
def google_the_link(uni_name):
    browser.execute_script('''window.open("http://google.com","_blank");''')
    #windows_before  = browser.current_window_handle
    #print("First Window Handle is : %s" %windows_before)
    browser.switch_to_window(browser.window_handles[-1])
    search_name=WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, 'q')))
    search_name.send_keys(uni_name)
    browser.find_element_by_id('lga').click()
    browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]').click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'q')))
    sag=browser.find_elements_by_class_name('r')
    #link (First Search result)
    link = sag[0].find_element_by_tag_name('a').get_attribute('href')
    return link



