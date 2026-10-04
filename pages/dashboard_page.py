from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    create_posting_link = (By.CSS_SELECTOR, "section.welcome-section a.common-btn.create")

    def click_create_new_interview_posting(self):
        self.find(self.create_posting_link).click()
