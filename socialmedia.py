from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SocialMedia:
    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.PATH = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(self.PATH)

    def create_gmail(self):
        self.driver.get(
            'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')


if __name__ == "__main__":
    pass
