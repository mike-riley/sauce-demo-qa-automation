from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCTS_TITLE = (
        By.XPATH,
        "//span[text()='Products']"
    )

    def login(self, username, password):
        self.driver.find_element(
            *self.USERNAME
        ).send_keys(username)

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(password)

        self.driver.find_element(
            *self.LOGIN_BUTTON
        ).click()

    def is_logged_in(self):
        try:
            self.wait_for_visible(
                self.PRODUCTS_TITLE
            )
            return True
        except:
            return False