from geninfo import get_website_info
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_gmail(data, phone):
    PATH = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "view_container"))
    )

    # Entering all the Information into the Google Account to Create Account
    fields = {'firstName': 'first_name', 'lastName': 'surname', 'username': 'username',
              'Passwd': 'password', 'ConfirmPasswd': 'password'}

    for field, value in fields.items():
        search = driver.find_element_by_id(field)
        search.send_keys(data.get(value))
        search.send_keys(Keys.RETURN)


if __name__ == "__main__":
    create_gmail(get_website_info(), 742)

