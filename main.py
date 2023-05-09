import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
PATH = Service("C:\\Users\\mufti\\OneDrive\\Documents\\Github\\Selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH, options=chrome_options)
driver.maximize_window()
driver.get("EnterWebsiteHere")
sleep(2)
search = driver.find_element(By.ID, "username")
search.send_keys("EnterUserNameHere")
search = driver.find_element(By.ID, "password")
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "field14_tadaBankInfo_accntTitle")))
search = driver.find_element(By.NAME, "submit").click()
sleep(2)

os.system('cls')
