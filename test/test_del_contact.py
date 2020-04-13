from model.add_new import AddNew


def test_delete_first_contact(app):
     if app.contacts.count() == 0:
          app.contacts.create_contact(AddNew(my_f_name="Mamont"))
     old_contacts = app.contacts.get_contact_list()
     app.contacts.delete_first_contact()
     new_contacts = app.contacts.get_contact_list()
     assert len(old_contacts) - 1 == len(new_contacts)


