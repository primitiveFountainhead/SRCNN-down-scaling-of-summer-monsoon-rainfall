"""
    A very simple python code to automate downloading of data from imd pune data set
    Download .25 degraa and 1 degree rainfall data
    Specify start year and end year

"""
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time



wait_time=5
url = 'https://imdpune.gov.in/Clim_Pred_LRF_New/Grided_Data_Download.html'
#The xpath to dropdown with .25 and 1 degree resultion for rainfall
drop_down_xpaths={.25:"/html/body/div/div[2]/div[2]/div/form[2]/select",1:"/html/body/div/div[2]/div[2]/div/form[3]/select"}
dwn_btn_path={.25:"/html/body/div/div[2]/div[2]/div/form[2]/input",1:"/html/body/div/div[2]/div[2]/div/form[3]/input"}

#specify start year and end year here
start_year = 2000
stop_year = 2002

# Initialise driver
DRIVER_PATH = "chromedriver.exe"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(DRIVER_PATH,options=options)
driver.get(url)


#Create dropdown select objects
dropdowns = {}
btn = {}

for deg,path in drop_down_xpaths.items():
    dropdowns[deg]=Select(driver.find_element("xpath",path))
    btn[deg]=driver.find_element("xpath",dwn_btn_path[deg])

    
for yr in tqdm(range(start_year, stop_year)):
    for deg,drp_dwn in dropdowns.items():
        drp_dwn.select_by_visible_text(str(yr))
        btn[deg].click()
        time.sleep(5)
         

    
    
    



