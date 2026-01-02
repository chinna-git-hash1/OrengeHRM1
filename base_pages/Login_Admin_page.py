from selenium import webdriver
import pytest
# from selenium.webdriver.common.by import By
#
#
# class Login_Admin_Page:
#     textbox_username_name="username"
#     textbox_password_name="password"
#     btn_login_xpath="//button[@type='submit']"
#
#     def __init__(self,driver):
#         self.driver=driver
#
#     def enter_username(self,username):
#         self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)
#
#     def enter_password(self, password):
#         self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)
#
#     def click_login(self):
#         self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    username_name = "username"
    password_name = "password"
    login_btn_xpath = "//button[@type='submit']"
    error_msg_xpath = "//p[contains(@class,'oxd-alert-content-text')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located((By.NAME, self.username_name))
        ).clear()
        self.driver.find_element(By.NAME, self.username_name).send_keys(username)

    def set_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located((By.NAME, self.password_name))
        ).clear()
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.login_btn_xpath))
        ).click()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.error_msg_xpath))
        ).text

