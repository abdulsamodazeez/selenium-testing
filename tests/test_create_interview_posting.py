import uuid
from conftest import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.job_posting_page import JobPostingPage


def test_user_can_create_an_interview_posting_with_every_detail(driver):
    login = LoginPage(driver)
    login.enter_email(USERNAME)
    login.click_continue()
    login.enter_password(PASSWORD)
    login.click_sign_in()
    assert login.welcome_is_displayed()

    DashboardPage(driver).click_create_new_interview_posting()

    posting = JobPostingPage(driver)
    posting.choose_write_description()
    posting.enter_description("Hiring a Senior QA Automation Engineer for the platform team.")
    posting.enter_job_title("Senior QA Automation Engineer")
    posting.enter_job_requisition("REQ-" + uuid.uuid4().hex[:6])
    posting.choose_location("San Francisco")
    posting.choose_experience()
    posting.enter_salary("120000")
    posting.enter_branch("SF Campus")
    posting.enter_additional_information("Hybrid role, three days on site.")
    posting.click_create_post()
    assert posting.post_created_is_displayed()
