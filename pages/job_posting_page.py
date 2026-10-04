from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class JobPostingPage(BasePage):
    write_description_tab = (By.XPATH, "//button[text()='Write or Paste Description']")
    description_editor = (By.CSS_SELECTOR, ".ql-editor")
    job_title = (By.NAME, "jobTitle")
    job_requisition = (By.NAME, "jobRequisition")
    location = (By.CSS_SELECTOR, "input[placeholder='Search for a city or region']")
    first_location_suggestion = (By.CSS_SELECTOR, "li:first-child")
    experience_dropdown = (By.CSS_SELECTOR, ".custom-select__control")
    experience_option = (By.XPATH, "//div[@role='option' and text()='0-1 Years']")
    salary = (By.NAME, "salary_range")
    branch = (By.CSS_SELECTOR, "input[placeholder='e.g. SF Campus, Asia Branch, Sutter St']")
    additional_information = (By.TAG_NAME, "textarea")
    create_post_button = (By.XPATH, "//button[text()='Create Post']")
    post_created_heading = (By.XPATH, "//h2[contains(., 'Interview Post Created!')]")

    def choose_write_description(self):
        self.find(self.write_description_tab).click()

    def enter_description(self, text):
        self.find(self.description_editor).send_keys(text)

    def enter_job_title(self, text):
        self.find(self.job_title).send_keys(text)

    def enter_job_requisition(self, text):
        self.find(self.job_requisition).send_keys(text)

    def choose_location(self, city):
        self.find(self.location).send_keys(city)
        self.find(self.first_location_suggestion).click()

    def choose_experience(self):
        self.find(self.experience_dropdown).click()
        self.find(self.experience_option).click()

    def enter_salary(self, text):
        self.find(self.salary).send_keys(text)

    def enter_branch(self, text):
        self.find(self.branch).send_keys(text)

    def enter_additional_information(self, text):
        self.find(self.additional_information).send_keys(text)

    def click_create_post(self):
        self.find(self.create_post_button).click()

    def post_created_is_displayed(self):
        return self.find(self.post_created_heading).is_displayed()
