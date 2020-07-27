from string import capwords
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SocialMedia:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.PATH = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(self.PATH)

    def create_gmail(self):
        self.driver.get(
            'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')

        first_name = self.driver.find_element_by_id("firstName")
        first_name.send_keys(self.first_name)
        first_name.send_keys(Keys.RETURN)

        last_name = self.driver.find_element_by_id("lastName")
        last_name.send_keys(self.last_name)
        last_name.send_keys(Keys.RETURN)

        username = self.driver.find_element_by_id("username")
        username.send_keys(self.username)
        username.send_keys(Keys.RETURN)

        password = self.driver.find_element_by_name("Passwd")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

        confirm = self.driver.find_element_by_name("ConfirmPasswd")
        confirm.send_keys(self.password)
        confirm.send_keys(Keys.RETURN)


if __name__ == "__main__":
    gmail = SocialMedia("Anna love", "anna12723492", "1234Anna")
    gmail.create_gmail()
