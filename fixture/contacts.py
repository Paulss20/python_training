from selenium.webdriver.support.ui import Select
from model.add_new import AddNew
import re


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

#     contact_cache = None

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
          self.change_field_contact_value("email3", add_new.my_third_mail)
          self.change_field_contact_value("homepage", add_new.my_homepage)
          wd.find_element_by_name("bday").click()
          Select(wd.find_element_by_name("bday")).select_by_visible_text("7")
          wd.find_element_by_xpath("//option[@value='7']").click()
          wd.find_element_by_name("bmonth").click()
          Select(wd.find_element_by_name("bmonth")).select_by_visible_text("August")
          wd.find_element_by_xpath("//option[@value='August']").click()
          self.change_field_contact_value("byear", add_new.my_byear)
          self.change_field_contact_value("address2", add_new.my_home_address)
          self.change_field_contact_value("phone2", add_new.my_secondary_phone)
          self.change_field_contact_value("notes", add_new.my_notes)

     def create_contact(self, add_new):
          wd = self.app.wd
          self.open_add_new_page()
          self.fill_contact_form(add_new)
          # submit add_new creation
          wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
#          self.return_to_home_page()
          self.open_home_tab()
          self.contact_cache = None

     def open_home_tab(self):
          wd = self.app.wd
          if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add")) > 0):
               wd.find_element_by_link_text("home").click()

     def select_first_contact(self):
          wd = self.app.wd
          wd.find_element_by_name("selected[]").click()

     def select_contact_by_index(self, index):
          wd = self.app.wd
          wd.find_elements_by_name("selected[]")[index].click()

     def delete_first_contact(self):
          self.delete_contact_by_index(0)

     def delete_contact_by_index(self, index):
          wd = self.app.wd
          self.open_home_tab()
          self.select_contact_by_index(index)
          # submit deletion
          wd.find_element_by_xpath("//input[@value='Delete']").click()
          wd.switch_to_alert().accept()
          # return to home page
          self.open_home_tab()
          self.contact_cache = None

     def modify_first_contact(self):
          self.modify_contact_by_index(0)

     def modify_contact_by_index(self, index, new_contact_data):
          wd = self.app.wd
          self.open_home_tab()
          self.select_contact_by_index(index)
          # open modification form
          wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
          # fill group form
          self.fill_contact_form(new_contact_data)
          # submit modification
          wd.find_element_by_name("update").click()
          self.open_home_tab()
          self.contact_cache = None

     def return_to_home_page(self):
          wd = self.app.wd
          if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add")) > 0):
               wd.find_element_by_link_text("home").click()

     def count(self):
         wd = self.app.wd
         self.open_home_tab()
         return len(wd.find_elements_by_name("selected[]"))

     contact_cache = None  # in contact_cache we will put the information read from the browser window

     def get_contact_list(self):
          if self.contact_cache is None:
               wd = self.app.wd
               self.open_home_tab()
               self.contact_cache = []
               for row in wd.find_elements_by_name("entry"):
                    cells = row.find_elements_by_tag_name("td")
                    text_lastname = cells[1].text
                    text_firstname = cells[2].text
                    id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                    text_address = cells[3].text
                    all_emails = cells[4].text
                    all_phones = cells[5].text
                    self.contact_cache.append(AddNew(my_l_name=text_lastname, my_f_name=text_firstname, my_id=id,
                                                     my_home_address=text_address,
                                                     all_emails_from_home_page=all_emails,
                                                     all_phones_from_home_page=all_phones))
          return list(self.contact_cache)

     def open_contact_to_edit_by_index(self, index):
          wd = self.app.wd
          self.open_home_tab()
          row = wd.find_elements_by_name("entry")[index]
          cell = row.find_elements_by_tag_name("td")[7]
          cell.find_element_by_tag_name("a").click()

     def open_contact_view_by_index(self, index):
          wd = self.app.wd
          self.open_home_tab()
          row = wd.find_elements_by_name("entry")[index]
          cell = row.find_elements_by_tag_name("td")[6]
          cell.find_element_by_tag_name("a").click()

     def get_contact_info_from_edit_page(self, index):
          wd = self.app.wd
          self.open_contact_to_edit_by_index(index)
          firstname = wd.find_element_by_name("firstname").get_attribute("value")
          lastname = wd.find_element_by_name("lastname").get_attribute("value")
          id_contact = wd.find_element_by_name("id").get_attribute("value")
          home_phone = wd.find_element_by_name("home").get_attribute("value")
          mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
          work_phone = wd.find_element_by_name("work").get_attribute("value")
          phone2 = wd.find_element_by_name("phone2").get_attribute("value")
          home_address = wd.find_element_by_name("address").text
          company_email = wd.find_element_by_name("email").get_attribute("value")
          second_email = wd.find_element_by_name("email2").get_attribute("value")
          third_email = wd.find_element_by_name("email3").get_attribute("value")
          return AddNew(my_f_name=firstname, my_l_name=lastname, my_id=id_contact, my_h_telefon=home_phone,
                         my_mobile=mobile_phone, my_work_telefon=work_phone, my_secondary_phone=phone2,
                        my_home_address=home_address, my_company_mail=company_email,
                        my_second_mail=second_email, my_third_mail=third_email)

     def get_contact_from_view_page(self, index):
          wd = self.app.wd
          self.open_contact_view_by_index(index)
          text = wd.find_element_by_id("content").text
          home_phone = re.search("H: (.*)", text).group(1)
          work_phone = re.search("W: (.*)", text).group(1)
          mobile_phone = re.search("M: (.*)", text).group(1)
          phone2 = re.search("P: (.*)", text).group(1)
          return AddNew(my_h_telefon=home_phone, my_mobile=mobile_phone,
                        my_work_telefon=work_phone, my_secondary_phone=phone2)