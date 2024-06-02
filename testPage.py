from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO = (By.CSS_SELECTOR, """#app > main > nav > ul > li.svelte-1rc85o5.mdc-menu-surface--anchor > a""")
    LOCATOR_NEW_POST_BTN = (By.CSS_SELECTOR, "#create-btn")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.CSS_SELECTOR, "#create-item > div > div > div:nth-child(7) > div > button")
    LOCATOR_RES_TEXT = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_MESSAGE_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_SEND_BTN = (By.CSS_SELECTOR, """#contact > div.submit > button > div""")

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_user_text(self):
        user_filed = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=2)
        text = user_filed.text
        logging.info(f"We find text {text}")
        return text

    def click_new_post_btn(self):
        logging.info("Click create new post button")
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_title(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def enter_description(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def click_save_btn(self):
        wait = WebDriverWait(self.driver, 10)
        save_btn = wait.until(EC.visibility_of_element_located(TestSearchLocators.LOCATOR_SAVE_BTN))
        ActionChains(self.driver).move_to_element(save_btn).perform()
        save_btn.click()

    def get_res_text(self):
        result_text_element = self.driver.find_element(TestSearchLocators.LOCATOR_RES_TEXT)
        text = result_text_element.text
        return text

    def test_contact_us_button(self):
        contact_us_button = self.driver.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN)
        contact_us_button.click()

    def test_contact_us_name_field(self, word):
        name_field = self.driver.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        name_field.send_keys(word)

    def test_contact_us_email_field(self, word):
        email_field = self.driver.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(word)

    def test_contact_us_message_field(self, word):
        message_field = self.driver.find_element(TestSearchLocators.LOCATOR_MESSAGE_FIELD)
        message_field.send_keys(word)

    def test_contact_us_send_button(self):
        send_button = self.driver.find_element(TestSearchLocators.LOCATOR_SEND_BTN)
        send_button.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert "Form successfully submitted" in alert.text
        alert.accept()