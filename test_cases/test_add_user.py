import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base_pages.Home_page import Login_AdminPage
from base_pages.Login_Admin_page import LoginPage
# from base_pages.admin_page import DashboardPage
from selenium.webdriver.support import expected_conditions as EC


def test_add_user(setup):
    driver=setup
    login = LoginPage(driver)
    login.set_username("Admin")
    login.set_password("admin123")
    login.click_login()

    admin_page = Login_AdminPage(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, admin_page.admin_xpath))
    )
    # dashboard.click_admin_button()
    # time.sleep(3)
    #
    # admin_page = Login_AdminPage(driver)
    # admin_page.click_add_button()
    # time.sleep(3)
    admin_page.click_admin_button()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, admin_page.click_add_xpath))
    )
    admin_page.click_add_button()
    admin_page.select_user_role("ESS")
    admin_page.enter_employee_name("Ranga  Akunuri")
    admin_page.select_status("Enabled")
    admin_page.enter_username("linda.test")
    admin_page.enter_password("chinna@123")
    admin_page.enter_confirm_password("chinna@123")
    admin_page.click_save()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[text()='linda.test']"))
    )
    assert "linda.test" in driver.page_source
    time.sleep(5)

