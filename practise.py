from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pytest
driver =webdriver.Edge(EdgeChromiumDriverManager().install())
driver.maximize_window()
driver.get("https://www.makemytrip.com/flights/")
#driver.find_element(By.XPATH,"//div[@class='hsBackDrop']").click()
driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/div/div[2]/div[2]/div[1]/ul/li[3]").click()
driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[1]").click()
driver.find_element(By.XPATH,"//input[@placeholder='From']").send_keys("hyderabad")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='react-autowhatever-1-section-0-item-0']").click()
driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/input").send_keys("new delhi")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='react-autowhatever-1-section-0-item-0']").click()
time.sleep(5)
# driver.find_element(By.XPATH,"//div[@class = 'fsw_inputBox dates inactiveWidget activeWidget' or @class='fsw_inputBox dates inactiveWidget ']/label").click()
# time.sleep(5)
driver.find_element(By.XPATH,"//label[@for='departure']").click()

