from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    email = (By.NAME, "email")
    continue_button = (By.XPATH, "//button[text()='Continue']")
    password = (By.NAME, "password")
    sign_in_button = (By.XPATH, "//button[text()='Sign In']")
    welcome_heading = (By.XPATH, "//h2[contains(., 'Welcome SimpleTest!')]")

    def enter_email(self, value):
        self.find(self.email).send_keys(value)

    def click_continue(self):
        self.find(self.continue_button).click()

    def enter_password(self, value):
        self.find(self.password).send_keys(value)

    def click_sign_in(self):
        self.find(self.sign_in_button).click()

    def welcome_is_displayed(self):
        return self.find(self.welcome_heading).is_displayed()
