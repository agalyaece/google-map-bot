# import required modules
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


SOURCE = "Tiruchirappalli"
DESTINATION = "Tirunelveli"


# assign url in the webdriver object
driver = webdriver.Firefox()
driver.get("https://www.google.com/maps/@10.7773952,78.6530304,12z?entry=ttu")
sleep(5)


# search locations
def search_place():
    place = driver.find_element(By.ID, "searchboxinput")
    place.send_keys(SOURCE)
    sleep(5)
    submit = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button/span")
    submit.click()
    sleep(4)


search_place()


# get directions
def directions():
    sleep(4)
    directions_1 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span")
    directions_1.click()
    sleep(4)


directions()


# /find place
def find():
    sleep(6)
    find_1 = driver.find_element(
        By.CLASS_NAME, "tactile-searchbox-input")
    find_1.send_keys(DESTINATION)
    sleep(3)
    search = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()
    sleep(3)


find()


# get transportation details
def kilometers():
    sleep(5)
    Totalkilometers = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[2]/div")
    print("Total Kilometers:", Totalkilometers.text)
    sleep(5)

#
#
kilometers()
