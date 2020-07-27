from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CreateSocialMedia:
    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password

    def create_gmail(self):
        PATH = "/usr/local/bin/chromedriver"
        driver = webdriver.Chrome(PATH)
        driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")


if __name__ == "__main__":
    pass
