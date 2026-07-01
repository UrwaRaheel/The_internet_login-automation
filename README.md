# The Internet Login Automation Project

##  Project Overview

This project is an automated testing framework built using **Python, Selenium WebDriver, Pytest, and Page Object Model (POM)**. It automates the login functionality of **The Internet** demo website.

Website: https://the-internet.herokuapp.com/login

---

##  Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* VS Code

---

##  Automated Test Cases

### Login Test Cases

* Valid Login
* Invalid Username
* Invalid Password
* Empty Username
* Empty Password
* Empty Credentials

### Logout Test Case

* Verify that the user is redirected to the Login page after clicking the Logout button.

---

##  Features

* Page Object Model (POM) implementation
* Reusable page classes
* Explicit Waits using WebDriverWait
* Automated validation using Assertions
* Easy to maintain and scalable framework

---

##  How to Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run All Tests

```bash
pytest -v
```

### Run a Specific Test File

```bash
pytest tests/test_login.py -v
```

---

##  Application Under Test

Website: https://the-internet.herokuapp.com/login

**Valid Credentials**

* Username: `tomsmith`
* Password: `SuperSecretPassword!`

---

##  Author

**Urwa Raheel**

Aspiring QA Automation Engineer | Python | Selenium | Pytest | Automation Testing Enthusiast
