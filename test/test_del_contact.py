from model.add_new import AddNew


def test_delete_first_contact(app):
     if app.contacts.count() == 0:
          app.contacts.create_contact(AddNew(my_l_name="Elephant", my_f_name="Mamont"))
     app.contacts.delete_first_contact()

