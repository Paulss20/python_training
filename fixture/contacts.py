from selenium.webdriver.support.ui import Select
from model.add_new import AddNew


class ContactsHelper:

     def __init__(self, app):
          self.app = app

     def open_add_new_page(self):
          wd = self.app.wd
          wd.find_element_by_link_text("add new").click()

     def change_field_contact_value(self, field_name, text):
          wd = self.app.wd
          if text is not None:
               wd.find_element_by_name(field_name).click()
               wd.find_element_by_name(field_name).clear()
               wd.find_element_by_name(field_name).send_keys(text)

     def fill_contact_form(self, add_new):
          wd = self.app.wd
          self.change_field_contact_value("firstname", add_new.my_f_name)
          self.change_field_contact_value("middlename", add_new.my_m_name)
          self.change_field_contact_value("lastname", add_new.my_l_name)
          self.change_field_contact_value("nickname", add_new.my_nickname)
          self.change_field_contact_value("company", add_new.my_company)
          self.change_field_contact_value("address", add_new.work_address)
          self.change_field_contact_value("home", add_new.my_h_telefon)
          self.change_field_contact_value("mobile", add_new.my_mobile)
          self.change_field_contact_value("work", add_new.my_work_telefon)
          self.change_field_contact_value("fax", add_new.my_fax)
          self.change_field_contact_value("email", add_new.my_company_mail)
          self.change_field_contact_value("email2", add_new.my_second_mail)
          self.change_field_contact_value("homepage", add_new.my_homepage)
          wd.find_element_by_name("bday").click()
          Select(wd.find_element_by_name("bday")).select_by_visible_text("7")
          wd.find_element_by_xpath("//option[@value='7']").click()
          wd.find_element_by_name("bmonth").click()
          Select(wd.find_element_by_name("bmonth")).select_by_visible_text("August")
          wd.find_element_by_xpath("//option[@value='August']").click()
          self.change_field_contact_value("byear", add_new.my_byear)
          self.change_field_contact_value("address2", add_new.my_home_address)
          self.change_field_contact_value("phone2", add_new.my_second_address)
          self.change_field_contact_value("notes", add_new.my_notes)

     def create_contact(self, add_new):
          wd = self.app.wd
          self.open_add_new_page()
          self.fill_contact_form(add_new)
          # submit add_new creation
          wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
          self.return_to_home_page()
          self.open_home_tab()

     def open_home_tab(self):
          wd = self.app.wd
          if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add")) > 0):
               wd.find_element_by_link_text("home").click()

     def select_first_contact(self):
          wd = self.app.wd
          wd.find_element_by_name("selected[]").click()

     def delete_first_contact(self):
          wd = self.app.wd
          self.open_home_tab()
          self.select_first_contact()
          # submit deletion
          wd.find_element_by_xpath("//input[@value='Delete']").click()
          wd.switch_to_alert().accept()
          # return to home page
          self.open_home_tab()

     def modify_first_contact(self, new_contact_data):
          wd = self.app.wd
          self.open_home_tab()
          self.select_first_contact()
          # open modification form
          wd.find_element_by_xpath("//img[@alt='Edit']").click()
          # fill group form
          self.fill_contact_form(new_contact_data)
          # submit modification
          wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
          self.open_home_tab()

     def return_to_home_page(self):
          wd = self.app.wd
          if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add")) > 0):
               wd.find_element_by_link_text("home").click()
#               wd.find_element_by_link_text("home page").click()

     def count(self):
         wd = self.app.wd
         self.open_add_new_page()
         return len(wd.find_elements_by_name("selected[]"))

     def get_contact_list(self):
          wd = self.app.wd
          self.open_home_tab()
          contacts = []
#          for element in wd.find_elements_by_css_selector("tr[name=entry]"):
          for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
               cells = element.find_elements_by_tag_name("td")
               lastname = cells[1].text
               firstname = cells[2].text
               id = element.find_element_by_name("selected[]").get_attribute("value")
               contacts.append(AddNew(my_l_name=lastname, my_f_name=firstname, my_id=id))
          return contacts

