from testpage import OperationsHelper
from selenium import webdriver
import logging
import yaml
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    name = testdata["username"]
    passwd = testdata["password"]


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(name)
    testpage.enter_pass(passwd)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {name}"


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title("testtitle")
    testpage.enter_content("testcontent")
    testpage.enter_description("testdesc")
    testpage.click_save_btn()
    time.sleep(2)
    assert testpage.get_res_text() == "testtitle"


def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationsHelper(browser)
    testpage.test_contact_us_button()
    testpage.test_contact_us_name_field("testname")
    testpage.test_contact_us_email_field("testemail@testemail.com")
    testpage.test_contact_us_message_field("testmessage")
    time.sleep(2)
    testpage.test_contact_us_send_button() == "Form successfully submitted"