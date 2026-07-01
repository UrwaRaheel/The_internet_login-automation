from pages.Login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.secure_page import SecurePage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.login("tomsmith", "SuperSecretPassword!")

    WebDriverWait(driver, 10).until(
        EC.url_contains("/secure")
    )
def test_innvalid_usernamelogin(driver):
    login = LoginPage(driver)
    login.login("tom", "SuperSecretPassword!")

    assert "Your username is invalid!" in driver.page_source
def test_innvalid_passwordlogin(driver):
    login = LoginPage(driver)
    login.login("tomsmith", "Super")

    assert "Your password is invalid!" in driver.page_source
def test_innvalid_emptyusernamelogin(driver):
    login = LoginPage(driver)
    login.login("", "SuperSecretPassword!")

    assert "Your username is invalid!" in driver.page_source
def test_innvalid_emptypasswordlogin(driver):
    login = LoginPage(driver)
    login.login("tomsmith", "")

    assert "Your password is invalid!" in driver.page_source
def test_logout(driver):
    login = LoginPage(driver)
    login.login("tomsmith", "SuperSecretPassword!")
    WebDriverWait(driver, 10).until(
        EC.url_contains("/secure")
    )
   

    secure = SecurePage(driver)
    secure.logout()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    