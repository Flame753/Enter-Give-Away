import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_website_info():
    PATH = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.name-generator.org.uk/username/")

    driver.find_element_by_id("fill_all").click()

    # Adding the information into data
    data = {}
    fields = ['first_name', 'middle_name', 'surname', 'gender',
              'birth_year', 'adj1', 'adj2', 'location', 'job', 'likes']
    for field in fields:
        data[field] = driver.find_element_by_name(field).get_attribute("value")

    # Setting up and going to the next page to create the username
    driver.find_element_by_name("allow_underscores").click()
    driver.find_element_by_name("allow_dots").click()
    driver.find_element_by_id("quick_submit").click()
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    # Getting the username from the site then add it to the data
    user = []
    usernames = main.find_elements_by_class_name("username_item")
    for username in usernames:
        user.append(username.text)

    data['username'] = random.choice(user)
    return data


if __name__ == "__main__":
    print(get_website_info())
