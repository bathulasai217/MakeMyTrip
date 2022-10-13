import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResults:
    text_popup_xpath = "//*[@id='root']/div/div[2]/div[2]/div[2]/div/span"
    # "//span[@class='lock-price-illustrationIconV2 appendBottom12']"
    text_ticket_fare_xpath = "//header[@class='search-bar']//li[3]"
    text_flight_name_xpath = "//div[@class = 'listingCardWrap ']/div/div/div/div/div[2]/div/div/p[@class='boldFont blackText airlineName']"
    text_flight_d_time_xpath = "//div[@class = 'listingCardWrap ']/div/div/div/div/div[2]/div[2]/label/div/div/div/div[@class='flexOne timeInfoLeft']/p[1]/span"
    text_flight_duration_xpath = "//div[@class = 'listingCardWrap ']/div/div/div/div/div[2]/div[2]/label/div/div/div/div[@class='stop-info flexOne']/p"
    def __init__(self, driver,wait):
        self.wait = wait
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
    def set_alert(self):
        alert = self.driver.find_element(By.XPATH, self.text_popup_xpath)
        if alert.is_displayed():
            alert.click()
        # self.driver.switch_to.alret.accept()
        # self.driver.switch_to.frame()

    def set_ticketfare(self):
        self.driver.find_element(By.XPATH, self.text_ticket_fare_xpath)



