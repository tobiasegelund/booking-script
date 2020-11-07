from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import schedule
from credentials import username, password


usr = username # Indsæt dit eget username
pwd = password # Insæt dit eget password

driver = webdriver.Chrome(ChromeDriverManager().install())

def job():
    driver.get('https://booking.sport-solutions.dk/login/da-DK?issue=false')
    print ("Opened booking-site")
    sleep(1)

    username_box = driver.find_element_by_id('username')
    username_box.send_keys(usr)
    print ("Email Id entered")
    sleep(1)

    password_box = driver.find_element_by_id('password')
    password_box.send_keys(pwd)
    print ("Password entered")
    sleep(1)

    login_box = driver.find_element_by_xpath("//form[1]/button[1]")
    login_box.click()
    sleep(3)

    try:
        driver.get('https://booking.sport-solutions.dk/main/weekCalendar')
        sleep(3)

    except:
        pass
    try:
        driver.get('https://booking.sport-solutions.dk/main/weekCalendar')
        sleep(3)
    except:
        pass

    try:
        arrow_move = driver.find_element_by_xpath("//div[@class='fc-toolbar']/div[@class='fc-right']/div[@class='fc-button-group'][2]")
        arrow_move.click()
        sleep(3)
        arrow_move.click()
        sleep(3)

        type_box = Select(driver.find_element_by_xpath("//div[@id='selector_type']/select[1]"))
        type_box.select_by_index(1)
        sleep(1)

    except:
        pass


def book():

    kategori_box = Select(driver.find_element_by_xpath("//select[@ng-model='selectedCategory']"))
    kategori_box.select_by_index(3)
    sleep(1)


    try:
        padel_table = driver.find_element_by_xpath("//div[@class='fc-view-container']/div[@class='fc-view fc-basicWeek-view fc-basic-view']/table/tbody[@class='fc-body']/tr/td/div[@class='fc-day-grid-container']/div[@class='fc-day-grid']/div[@class='fc-row fc-week fc-widget-content']/div[@class='fc-content-skeleton']/table/tbody/tr[13]/td[1]")
        padel_table.click()
        sleep(1)

        tilmeld = driver.find_element_by_xpath("//div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-footer ng-scope']/button[@ng-click='bookEvent()']")
        tilmeld.click()
        sleep(1)
    except:
        pass

    try:
        padel_table = driver.find_element_by_xpath("//div[@class='fc-view-container']/div[@class='fc-view fc-basicWeek-view fc-basic-view']/table/tbody[@class='fc-body']/tr/td/div[@class='fc-day-grid-container']/div[@class='fc-day-grid']/div[@class='fc-row fc-week fc-widget-content']/div[@class='fc-content-skeleton']/table/tbody/tr[14]/td[1]")
        padel_table.click()
        sleep(1)

        tilmeld = driver.find_element_by_xpath("//div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-footer ng-scope']/button[@ng-click='bookEvent()']")
        tilmeld.click()
        sleep(1)
    except:
        pass

    try:
        padel_table = driver.find_element_by_xpath("//div[@class='fc-view-container']/div[@class='fc-view fc-basicWeek-view fc-basic-view']/table/tbody[@class='fc-body']/tr/td/div[@class='fc-day-grid-container']/div[@class='fc-day-grid']/div[@class='fc-row fc-week fc-widget-content']/div[@class='fc-content-skeleton']/table/tbody/tr[15]/td[1]")
        padel_table.click()
        sleep(1)

        tilmeld = driver.find_element_by_xpath("//div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-footer ng-scope']/button[@ng-click='bookEvent()']")
        tilmeld.click()
        sleep(1)
    except:
        pass

    driver.quit()
    print("Finished")


schedule.every().day.at("23:59").do(job)
schedule.every().day.at("00:00").do(job)

while True:
    schedule.run_pending()
    sleep(1)
