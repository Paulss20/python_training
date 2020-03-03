# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.webdriver import WebDriver
from add_new import AddNew
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_new(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_new(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.fill_add_new_form(wd, AddNew(my_f_name="Sergei", my_m_name="Fedorovich", my_l_name="Semenov", my_nickname="try",
                               my_company="Big company", work_address="SPb, Fuchika str, 15", my_h_telefon="11111111",
                               my_mobile="2222222222", my_work_telefon="3333333333", my_fax="4444444444",
                               my_company_mail="big.company@gg.com", my_second_mail="b_company@gg.com",
                               my_homepage="www.big-company.su", my_byear="1985", my_home_address="SPb, Nevski str, 98",
                               my_second_address="SPb, Pushkin, Gogol str, 87", my_notes="fff"))
        self.logout(wd)

    def test_add_empty_new(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.fill_add_new_form(wd, AddNew(my_f_name="", my_m_name="", my_l_name="", my_nickname="",
                               my_company="", work_address="", my_h_telefon="",
                               my_mobile="", my_work_telefon="", my_fax="",
                               my_company_mail="", my_second_mail="",
                               my_homepage="", my_byear="", my_home_address="",
                               my_second_address="", my_notes=""))
        self.logout(wd)

    def logout(self, wd):
         wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
         wd.find_element_by_link_text("home page").click()

    def fill_add_new_form(self, wd, add_new):
         self.open_add_new_page(wd)
         # fill add_new form
         wd.find_element_by_name("firstname").click()
         wd.find_element_by_name("firstname").clear()
         wd.find_element_by_name("firstname").send_keys(add_new.my_f_name)
         wd.find_element_by_name("middlename").click()
         wd.find_element_by_name("middlename").clear()
         wd.find_element_by_name("middlename").send_keys(add_new.my_m_name)
         wd.find_element_by_name("lastname").click()
         wd.find_element_by_name("lastname").clear()
         wd.find_element_by_name("lastname").send_keys(add_new.my_l_name)
         wd.find_element_by_name("nickname").click()
         wd.find_element_by_name("nickname").clear()
         wd.find_element_by_name("nickname").send_keys(add_new.my_nickname)
         wd.find_element_by_name("company").click()
         wd.find_element_by_name("company").clear()
         wd.find_element_by_name("company").send_keys(add_new.my_company)
         wd.find_element_by_name("address").click()
         wd.find_element_by_name("address").clear()
         wd.find_element_by_name("address").send_keys(add_new.work_address)
         wd.find_element_by_name("home").click()
         wd.find_element_by_name("home").clear()
         wd.find_element_by_name("home").send_keys(add_new.my_h_telefon)
         wd.find_element_by_name("mobile").click()
         wd.find_element_by_name("mobile").clear()
         wd.find_element_by_name("mobile").send_keys(add_new.my_mobile)
         wd.find_element_by_name("work").click()
         wd.find_element_by_name("work").clear()
         wd.find_element_by_name("work").send_keys(add_new.my_work_telefon)
         wd.find_element_by_name("fax").click()
         wd.find_element_by_name("fax").clear()
         wd.find_element_by_name("fax").send_keys(add_new.my_fax)
         wd.find_element_by_name("email").click()
         wd.find_element_by_name("email").clear()
         wd.find_element_by_name("email").send_keys(add_new.my_company_mail)
         wd.find_element_by_name("email2").click()
         wd.find_element_by_name("email2").clear()
         wd.find_element_by_name("email2").send_keys(add_new.my_second_mail)
         wd.find_element_by_name("homepage").click()
         wd.find_element_by_name("homepage").clear()
         wd.find_element_by_name("homepage").send_keys(add_new.my_homepage)
         wd.find_element_by_name("bday").click()
         Select(wd.find_element_by_name("bday")).select_by_visible_text("7")
         wd.find_element_by_xpath("//option[@value='7']").click()
         wd.find_element_by_name("bmonth").click()
         Select(wd.find_element_by_name("bmonth")).select_by_visible_text("August")
         wd.find_element_by_xpath("//option[@value='August']").click()
         wd.find_element_by_name("byear").click()
         wd.find_element_by_name("byear").clear()
         wd.find_element_by_name("byear").send_keys(add_new.my_byear)
         wd.find_element_by_name("address2").click()
         wd.find_element_by_name("address2").clear()
         wd.find_element_by_name("address2").send_keys(add_new.my_home_address)
         wd.find_element_by_name("phone2").click()
         wd.find_element_by_name("phone2").clear()
         wd.find_element_by_name("phone2").send_keys(add_new.my_second_address)
         wd.find_element_by_name("notes").click()
         wd.find_element_by_name("notes").clear()
         wd.find_element_by_name("notes").send_keys(add_new.my_notes)
         # submit add_new creation
         wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
         self.return_to_home_page(wd)

    def open_add_new_page(self, wd):
         wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
         self.open_home_page(wd)
         wd.find_element_by_name("user").click()
         wd.find_element_by_name("user").clear()
         wd.find_element_by_name("user").send_keys(username)
         wd.find_element_by_name("pass").clear()
         wd.find_element_by_name("pass").send_keys(password)
         wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
         wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
