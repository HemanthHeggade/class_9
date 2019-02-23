import os
from selenium import webdriver
proj_path=os.getcwd()
driver_path=proj_path.replace("\\","/")+"/drivers"
print(driver_path)
driver=webdriver.Chrome(executable_path=driver_path+"/chromedriver.exe")
driver.get("http://facebook.com")
