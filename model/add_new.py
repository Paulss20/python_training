from sys import maxsize


class AddNew:
     def __init__(self, my_f_name=None, my_m_name=None, my_l_name=None, my_nickname=None, my_company=None,
                  work_address=None, my_h_telefon=None, my_mobile=None, my_work_telefon=None, my_fax=None,
                  my_company_mail=None, my_second_mail=None, my_third_mail=None, my_homepage=None, my_byear=None, my_home_address=None,
                  my_secondary_phone=None, my_notes=None, my_id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
          self.my_f_name = my_f_name
          self.my_m_name = my_m_name
          self.my_l_name = my_l_name
          self.my_nickname = my_nickname
          self.my_company = my_company
          self.work_address = work_address
          self.my_h_telefon = my_h_telefon
          self.my_mobile = my_mobile
          self.my_work_telefon = my_work_telefon
          self.my_fax = my_fax
          self.my_company_mail = my_company_mail
          self.my_second_mail = my_second_mail
          self.my_third_mail=my_third_mail
          self.my_homepage = my_homepage
          self.my_byear = my_byear
          self.my_home_address = my_home_address
          self.my_secondary_phone = my_secondary_phone
          self.my_notes = my_notes
          self.my_id = my_id
          self.all_phones_from_home_page = all_phones_from_home_page
          self.all_emails_from_home_page=all_emails_from_home_page

     def __repr__(self):
          return "%s:%s %s" % (self.my_id, self.my_f_name, self.my_l_name)

     def __eq__(self, other):
          return (self.my_id is None or other.my_id is None or self.my_id == other.my_id)\
                 and self.my_f_name == other.my_f_name and self.my_l_name == other.my_l_name

     def id_or_max(self):
          if self.my_id:
               return int(self.my_id)
          else:
               return maxsize