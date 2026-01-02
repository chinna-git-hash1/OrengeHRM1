# from selenium import webdriver
# import pytest
# from selenium.webdriver.common.by import By
#
# from base_pages.Login_Admin_page import Login_Admin_Page
#
# class Test_01_Admin_login:
#     admin_page_url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
#     username="Admin"
#     password="admin123"
#     invalid_username="admin1234"
#
#     def test_title_verification(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.admin_page_url)
#         act_title = self.driver.title
#         exp_title = "OrangeHRM"
#         if act_title == exp_title:
#             assert True
#             self.driver.close()
#         else:
#             self.driver.close()
#             assert False
#     def test_valid_admin_login(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.admin_page_url)
#         self.admin_lp = Login_Admin_Page(self.driver)
#         self.admin_lp.enter_username(self.username)
#         self.admin_lp.enter_password(self.password)
#         self.admin_lp.click_login()
#         act_dashboard_text= self.driver.find_element(By.XPATH,"//div[@class='oxd-brand-banner']").text
#         if act_dashboard_text == "OrangeHRM":
#             assert True
#             self.driver.close()
#         else:
#             self.driver.close()
#             assert False
#
#     def test_invalid_admin(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.admin_page_url)
#         self.admin_lp = Login_Admin_Page(self.driver)
#         self.admin_lp.enter_username(self.invalid_username)
#         self.admin_lp.enter_password(self.password)
#         self.admin_lp.click_login()
#         error_message = self.driver.find_element(By.XPATH,"//p[text()='Invalid credentials']").text
#         if error_message == "Invalid credentials":
#             assert True
#             self.driver.close()
#         else:
#             self.driver.close()
#             assert False
#
#
#
from base_pages.Login_Admin_page import LoginPage

class TestLogin:

    def test_title_verification(self,setup):

        self.driver = setup
        act_title = self.driver.title
        exp_title = "OrangeHRM"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification01.png")
            self.driver.close()
            assert False

    def test_valid_login(self, setup):
        self.driver = setup
        login = LoginPage(self.driver)

        login.set_username("Admin")
        login.set_password("admin123")
        login.click_login()

        assert "dashboard" in self.driver.current_url.lower()

    def test_invalid_login(self, setup):
        self.driver = setup
        login = LoginPage(self.driver)

        login.set_username("Admin")
        login.set_password("wrongpass")
        login.click_login()

        assert "Invalid credentials" in login.get_error_message()

    def test_empty_login(self, setup):
        self.driver = setup
        login = LoginPage(self.driver)

        login.click_login()

        assert "Required" in self.driver.page_source
