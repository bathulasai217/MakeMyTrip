from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
driver =webdriver.Edge(EdgeChromiumDriverManager().install())
driver.maximize_window()
wait=WebDriverWait(driver,10)
driver.get("https://www.makemytrip.com/flights/")
#wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='root']/div/div[2]/div/div/div/ul/li[1]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div/div[2]/div/div/div[2]/div[2]/div[1]/ul/li[3]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[1]"))).click()
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='From']"))).send_keys("hyderabad")
time.sleep(5)
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='react-autowhatever-1-section-0-item-0']"))).click()
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/input"))).send_keys("new")
time.sleep(5)
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='react-autowhatever-1-section-0-item-0']"))).click()


date_depature = "24-11-2022"
month_year = "November 2022"
for c in range(12):
    time.sleep(2)
    month = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'November 2022')]"))).text
    if month == month_year:
        days2 = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//*[@class = 'DayPicker-Day']")))
        for i in days2:
            print(i.text)
            #time.sleep(1)
            if i.get_attribute('aria-label')==("Thu Nov 10 2022"):
                i.click()
                time.sleep(2)
                print("clicked")
                break
        break
    else:
        arrow_button = driver.find_element(By.CSS_SELECTOR,"span[aria-label='Next Month']")
        arrow_button.click()















