from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, user, pwd):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username)
        )

        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()