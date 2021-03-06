import time
import accounts
from geninfo import get_website_info
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_gmail(data, phone_number):
    PATH = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')

    # Waiting until see something on page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "view_container")))
    time.sleep(1)
    # Entering all the Information into the Google Account to Create Account
    fields = {'firstName': 'first_name', 'lastName': 'surname', 'username': 'username',
              'Passwd': 'password', 'ConfirmPasswd': 'password'}

    for field, value in fields.items():
        if field in ['Passwd', 'ConfirmPasswd']:
            search = driver.find_element_by_name(field)
        else:
            search = driver.find_element_by_id(field)
        search.click()
        search.send_keys(data.get(value))
        search.send_keys(Keys.RETURN)
        time.sleep(1)

    # Waiting until its verification page is loaded and enters phone number
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "view_container")))
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "phoneNumberId")))
    search.send_keys(phone_number)
    search.send_keys(Keys.RETURN)

    while True:
        if input():
            break
    driver.close()


if __name__ == "__main__":
    create_gmail(get_website_info(), 0)
