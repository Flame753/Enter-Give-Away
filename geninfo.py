import time
import random

from selenium import webdriver


def get_website_info():
    PATH = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.name-generator.org.uk/username/")

    fill_website = driver.find_element_by_id("fill_all").click()

    data = {}
    fields = ['first_name', 'middle_name', 'surname', 'gender',
              'birth_year', 'adj1', 'adj2', 'location', 'job', 'likes']
    for field in fields:
        data[field] = driver.find_element_by_name(field).get_attribute("value")

    driver.find_element_by_name("allow_underscores").click()
    driver.find_element_by_name("allow_dots").click()
    driver.find_element_by_id("quick_submit").click()
    username = driver.find_elements_by_class_name("names")

    return data


if __name__ == "__main__":
    get_website_info()
