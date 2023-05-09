import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from colorama import Fore, Back, Style
from selenium.common.exceptions import NoSuchElementException

PATH = "C:\\Users\\mufti\\OneDrive\\Documents\\Github\\Selenium\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("EnterWebsiteHere")
sleep(2)
search = driver.find_element(By.ID, "j_username")
search.send_keys("EnterUserNameHere")
search = driver.find_element(By.ID, "j_password")
search.send_keys("EnterPasswordHere")
search = driver.find_element(By.NAME, "submit").click()
print("Login Successful!")
sleep(2)

os.system('cls')
print(Fore.GREEN+'------------------------------------------------------------Test Started!------------------------------------------------------------')
print(Fore.RESET)
