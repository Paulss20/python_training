# -*- coding: utf-8 -*-
from model.add_new import AddNew
import re

#def test_add_new(app, data_contacts): - если хотим грузить константные данные из заранее заготовленного файла
#def test_add_new(app, json_contacts): - если хотим грузить сгенерированные в отдельном файле данные


def test_add_new(app, db, json_contacts, check_ui):
     contact = json_contacts
     old_contacts = db.get_contact_list()
     app.contacts.create_contact(contact)
     new_contacts = db.get_contact_list()
     old_contacts.append(contact)
     assert sorted(old_contacts, key=AddNew.id_or_max) == sorted(new_contacts, key=AddNew.id_or_max)
     if check_ui:    # for a disabled check, where we compare the database information with the UI,
                     # we need to transform the list taken from the database (we take only id and name)
          new_contacts_ui = []
          for i in new_contacts:
               new_contacts_ui.append(AddNew(my_l_name=app.contacts.removing_spaces(i.my_l_name),
#                                             my_f_name=re.sub("  ", " ", i.my_f_name.strip()),
                                             my_f_name=app.contacts.removing_spaces(i.my_f_name),
                                             my_id=i.my_id,
#                                             work_address=i.work_address,
                                             all_phones_from_home_page=app.contacts.merge_phones_like_on_home_page(i),
                                             all_emails_from_home_page=app.contacts.merge_emails_like_on_home_page(i)
                                             )
                                      )
          assert sorted(new_contacts_ui, key=AddNew.id_or_max) == sorted(app.contacts.get_contact_list(), key=AddNew.id_or_max)




