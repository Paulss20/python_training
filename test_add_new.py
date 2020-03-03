# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.webdriver import WebDriver
from add_new import AddNew
import unittest
from contactsapp import ContactsApplication

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_new(unittest.TestCase):
    def setUp(self):
        self.app = ContactsApplication()

    def test_add_new(self):
        self.app.login(username="admin", password="secret")
        self.app.fill_add_new_form(AddNew(my_f_name="Sergei", my_m_name="Fedorovich", my_l_name="Semenov", my_nickname="try",
                               my_company="Big company", work_address="SPb, Fuchika str, 15", my_h_telefon="11111111",
                               my_mobile="2222222222", my_work_telefon="3333333333", my_fax="4444444444",
                               my_company_mail="big.company@gg.com", my_second_mail="b_company@gg.com",
                               my_homepage="www.big-company.su", my_byear="1985", my_home_address="SPb, Nevski str, 98",
                               my_second_address="SPb, Pushkin, Gogol str, 87", my_notes="fff"))
        self.app.logout()

    def test_add_empty_new(self):
        self.app.login(username="admin", password="secret")
        self.app.fill_add_new_form(AddNew(my_f_name="", my_m_name="", my_l_name="", my_nickname="",
                               my_company="", work_address="", my_h_telefon="",
                               my_mobile="", my_work_telefon="", my_fax="",
                               my_company_mail="", my_second_mail="",
                               my_homepage="", my_byear="", my_home_address="",
                               my_second_address="", my_notes=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
