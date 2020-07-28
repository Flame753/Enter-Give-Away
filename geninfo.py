import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_website():
    PATH = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.name-generator.org.uk/username/")

    go_random = driver.find_element_by_id("fill_all")
    go_random.click()

    data = {}
    fields = ['first_name', 'middle_name', 'surname', 'gender',
              'birth_year', 'adj1', 'adj2', 'location', 'job', 'likes']
    for field in fields:
        data[field] = driver.find_element_by_name(field).get_attribute("value")

    driver.find_element_by_name("allow_underscores").click()
    driver.find_element_by_name("allow_dots").click()
    driver.find_element_by_id("quick_submit").click()
    username = driver.find_elements_by_class_name("names")


if __name__ == "__main__":
    test.website()
    print(test.username)
