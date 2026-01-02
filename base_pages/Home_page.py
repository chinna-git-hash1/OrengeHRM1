from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_AdminPage:

    admin_xpath = "//span[text()='Admin']"
    click_add_xpath ="//button[contains(.,'Add')]"
    user_role_dropdown_xpath = "//label[text()='User Role']/following::div[1]"
    employee_name_input_xpath = "//input[@placeholder='Type for hints...']"
    status_dropdown_xpath = "//label[text()='Status']/following::div[1]"
    username_input_xpath="//label[text()='Username']/following::div[1]"
    password_input_xpath ="//label[text()='Password']/following::div[1]"
    confirm_password_xpath="//label[text()='Confirm Password']/following::div[1]"
    save_xpath="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def click_admin_button(self):
        self.driver.find_element(self.admin_xpath)
    def click_add_button(self):
        self.driver.find_element(self.click_add_xpath).click()

    def select_user_role(self,role):
        self.driver.find_element(self.user_role_dropdown_xpath).click()
        self.driver.find_element(By.XPATH, f"//div[@role='option']/span[text()='{role}']").click()

    def enter_employee_name(self,name):
        self.driver.find_element(self.username_input_xpath).send_keys(name)

    def select_status(self,status):
        self.driver.find_element(self.status_dropdown_xpath).click()
        self.driver.find_element(By.XPATH, f"//div[@role='option']/span[text()='{status}']").click()

    def enter_username(self,username):
        self.driver.find_element(self.username_input_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(self.password_input_xpath).send_keys(password)

    def enter_confirm_password(self,conf_password):
        self.driver.find_element(self.confirm_password_xpath).send(conf_password)

    def click_save(self):
        self.driver.find_element(self.save_xpath).click()

