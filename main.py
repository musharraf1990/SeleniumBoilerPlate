import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

PATH = "C:\\Users\\mufti\\OneDrive\\Documents\\Github\\Selenium\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
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
