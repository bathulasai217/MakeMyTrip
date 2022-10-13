import json

from selenium.webdriver.common.by import By

from pageObjects.ticketBookingPage import TicketBooking
from pageObjects.ticketSearchResultPage import SearchResults
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import _json


class Test001TicketDetails:
    baseURL = ReadConfig.getApplicationURL()  # "https://www.makemytrip.com/flights/"
    depatureLocation = ReadConfig.getDepartLocation()  # "Ahmedabad"
    destinyLocation = ReadConfig.getDestinyLocation()  # "New delhi"
    month_year = ReadConfig.getMonthYear()  # "January 2023"
    atttibute_value = ReadConfig.getDate()  # "Thu Jan 19 2023"
    titleflight = ReadConfig.getTitle()  # "Flight Booking, Flight Tickets Booking at Lowest Airfare | MakeMyTrip"
    logger = LogGen.loggen()

    def test_HomePageTitle(self, setup):
        self.logger.info("**************** Test001TicketDetails ********************")
        self.logger.info("**************** Verifying HomePAgeTitle ********************")
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.tp = TicketBooking(self.driver, self.wait)

        self.tp.set_loginEleminator()
        time.sleep(2)
        act_title = self.driver.title
        print(act_title)
        if act_title == self.titleflight:
            assert True
            self.driver.close()
            self.logger.info("**************** Home Page Tittle Passed ********************")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "homePageTitle.png")
            self.driver.close()
            self.logger.error("***************** Home Page Title Failed********************")
            assert False

    def test_flight_search(self, setup):
        self.logger.info("**************** Flight Search started ********************")
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.tp = TicketBooking(self.driver, self.wait)
        self.tp.set_loginEleminator()
        self.tp.set_departLocation(self.depatureLocation)
        self.logger.info("**************** Entered Departure Location details ********************")
        self.tp.set_destinyLocation(self.destinyLocation)
        self.logger.info("**************** Enter destiny Location details ********************")
        for c in range(12):
            time.sleep(2)
            month = self.driver.find_element(By.XPATH, "//div[@class='DayPicker-Caption']/div").text
            if month == self.month_year:
                days2 = self.driver.find_elements(By.XPATH, "//*[@class = 'DayPicker-Day']")
                for i in days2:
                    # print(i.text)
                    # time.sleep(1)
                    if i.get_attribute("aria-label") == (self.atttibute_value):
                        i.click()
                        time.sleep(2)
                        break
                break
            else:
                self.tp.set_monthsearch()
        self.logger.info("****************Date as been successfully selected ********************")
        self.tp.set_searchButton()
        self.sp = SearchResults(self.driver,self.wait)
        act_title = self.driver.title
        if act_title=="MakeMyTrip":
            assert True
            self.logger.info("*************** SearchPageTitle passed *****************")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"searchPageTitle.png")
            self.logger.info("****************** SearchPageTitle Verification Failed ***************")
            assert False

        time.sleep(2)
        self.sp.set_ticketfare()
        self.logger.info("**************** Student ticket Fare as been selected********************")
        time.sleep(2)
        flight_name = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.sp.text_flight_name_xpath)))
        flight_departure_time = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.sp.text_flight_d_time_xpath)))
        flight_duration = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.sp.text_flight_duration_xpath)))
        fNames = []
        fdpTime = []
        fdurTime = []
        result = {}
        for i in flight_name:
            fNames.append(i.text)
        #print(fNames)
        for j in flight_departure_time:
            fdpTime.append(j.text)
        #print(fdpTime)
        for k in flight_duration:
            fdurTime.append(k.text)
        #print(fdurTime)
        for i in range(len(fNames)):
            time.sleep(1)
            result[fNames[i]] = [fdpTime[i], fdurTime[i]]

            for r in result:
                row = {}
                row = {
                    'Flight_name': r,
                    'Departure_time': result[r][0],
                    'Duration': result[r][1]
                }
            print(json.dumps(row))



        self.driver.close()
