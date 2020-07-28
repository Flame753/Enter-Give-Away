import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GenInfo:
    def __init__(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.gender = None
        self.birth_year = None
        self.adj1 = None
        self.adj2 = None
        self.location = None
        self.job = None
        self.likes = None
        self.username = None
        self.password = None

    def gen_random_person(self):
        self.gen_full_name()
        self.gen_gender()
        self.gen_birth_year(15)
        self.gen_username()
        self.gen_password()

        return {'first_name': self.first_name,
                'middle_name': self.middle_name,
                'last_name': self.last_name,
                'gender': self.gender,
                'birth_year': self.birth_year,
                'username': self.username,
                'password': self.password}

    def gen_gender(self):
        self.gender = random.choice(['male', 'female'])

    def gen_full_name(self):
        with open('names.txt', 'r') as file:
            lis_of_names = file.readlines()
            self.first_name = random.choice(lis_of_names).split()[0]
            self.last_name = random.choice(lis_of_names).split()[1]
            if self.first_name.find('-') != -1:
                self.middle_name = self.first_name[self.first_name.find('-') + 1:]
                self.first_name = self.first_name[:self.first_name.find('-')]

    def gen_birth_year(self, min_age_group=0, max_age_group=65):
        current_year = int(time.ctime().split()[-1])
        self.birth_year = current_year - random.randint(min_age_group, max_age_group)

    def gen_username(self):
        self.username = self.first_name[0:1] + self.last_name + str(self.birth_year)[1:]

    def gen_password(self):
        self.password = None

    def website(self):
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
        self.username = driver.find_elements_by_class_name("names")


if __name__ == "__main__":
    test = GenInfo()
    test.gen_full_name()
    test.gen_gender()
    test.gen_birth_year(15)
    test.gen_username()

    #print(test.first_name, test.middle_name, test.last_name)
    #print(test.gender, test.birth_year)
    #print(test.username, test.password)

    test.website()
    print(test.username)
