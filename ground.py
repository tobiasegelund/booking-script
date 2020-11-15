from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
import schedule
from credentials import username, password


usr = username  # Insert your own username
pwd = password  # Insert your own password

driver = webdriver.Chrome(ChromeDriverManager().install())


def job():
    driver.get('https://booking.sport-solutions.dk/login/da-DK?issue=false')
    print("Opened booking site")
    sleep(1)

    username_box = driver.find_element_by_id('username')
    username_box.send_keys(usr)
    sleep(1)

    password_box = driver.find_element_by_id('password')
    password_box.send_keys(pwd)
    sleep(1)

    login_box = driver.find_element_by_xpath("//form[1]/button[1]")
    login_box.click()
    print("Logged in")
    sleep(5)

    try:
        driver.get('https://booking.sport-solutions.dk/main/weekCalendar')
        sleep(5)

    except:
        print('Could not find Calendar')

    try:
        arrow_move = driver.find_element_by_xpath("//div[@class='fc-toolbar']/div[@class='fc-right']/div[@class='fc-button-group'][2]")
        arrow_move.click()
        sleep(5)
        arrow_move.click()
        sleep(5)

        # # ONLY WHEN BOOKING ON MONDAY
        # arrow_move.click()
        # sleep(3)

        type_box = Select(driver.find_element_by_xpath("//div[@id='selector_type']/select[1]"))
        type_box.select_by_index(1)
        sleep(2)

    except:
        pass


def booking_hour(hour):
    padel_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[@class='fc-view-container']/div[@class='fc-view fc-basicWeek-view fc-basic-view']/table/tbody[@class='fc-body']/tr/td/div[@class='fc-day-grid-container']/div[@class='fc-day-grid']/div[@class='fc-row fc-week fc-widget-content']/div[@class='fc-content-skeleton']/table/tbody/tr[{hour}]/td[1]")))
    padel_table.click()

    try:
        tilmeld = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-footer ng-scope']/button[@ng-click='bookEvent()']")))
        tilmeld.click()

        print("Booked!")
        luk = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[3]/button")))
        luk.click()

    except:
        print("Could not find booking button")

        cancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-footer ng-scope']/button[@ng-click='cancel()']")))

        cancel.click()


def book():
    kategori_box = Select(driver.find_element_by_xpath("//select[@ng-model='selectedCategory']"))
    kategori_box.select_by_index(3)

    booking_hour(13)
    booking_hour(14)
    booking_hour(15)

    driver.quit()
    print("Finished")


schedule.every().day.at("23:59").do(job)
schedule.every().day.at("00:00").do(book)

while True:
    schedule.run_pending()
    sleep(1)
