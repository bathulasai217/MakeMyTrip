import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TicketBooking:
    text_depart_loc_click_xpath = "//span[normalize-space()='From']"
    text_depart_loc_search_xpath = "//input[contains(@placeholder,'From')]"
    text_depart_dest_loc_click_xpath = "//li[@id='react-autowhatever-1-section-0-item-0']"

    text_dest_loc_search_xpath = "//input[@placeholder='To']"
    text_flighticon_xpath = "//div[@class='loginModal displayBlock modalLogin dynHeight personal']"

    text_month_xpath = "//div[@class='DayPicker-Caption']/div"  # "//div[contains(text(),'November 2022')]"
    text_days_xpath = "//*[@class = 'DayPicker-Day']"
    text_arrow_click_css = "span[aria-label='Next Month']"

    text_click_search_xpath = "//a[contains(@class,'primaryBtn font24 latoBold widgetSearchBtn')]"
    text_select_fare_xpath = "//span[normalize-space()='Student']"

    text_logineleminator_xpath = "//body/div[@id='root']/div[@class='bgGradient webpSupport']/div[@class='minContainer']/div[1]"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.wait = WebDriverWait(self.driver, 10)

    def set_departLocation(self, departLocation):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.text_depart_loc_click_xpath))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.text_depart_loc_search_xpath))).send_keys(departLocation)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.text_depart_dest_loc_click_xpath))).click()

    def set_destinyLocation(self, destinyLocation):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.text_dest_loc_search_xpath))).send_keys(destinyLocation)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.text_depart_dest_loc_click_xpath))).click()

    def set_monthsearch(self):
        self.driver.find_element(By.CSS_SELECTOR, self.text_arrow_click_css).click()

    def set_searchButton(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.text_click_search_xpath))).click()

    def set_selectFare(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.text_select_fare_xpath))).click()

    def set_loginEleminator(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.text_logineleminator_xpath))).click()

