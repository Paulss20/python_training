from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from fixture.contact_session import ContactSessionHelper
from fixture.contacts import ContactsHelper


class ContactsApplication:

     def __init__(self):
          self.wd = WebDriver()
          self.wd.implicitly_wait(60)
          self.contact_session = ContactSessionHelper(self)
          self.contacts = ContactsHelper(self)

     def open_home_page(self):
          wd = self.wd
          wd.get("http://localhost/addressbook/")

     def destroy(self):
          self.wd.quit()

