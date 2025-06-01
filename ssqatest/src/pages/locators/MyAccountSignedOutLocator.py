from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:
    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[name="login"]')

    ERROR_UL = (By.CSS_SELECTOR, '.wc-block-components-notice-banner__content')