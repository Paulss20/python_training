from model.add_new import AddNew


def test_modify_contact_first_name(app):
    app.contacts.modify_first_contact(AddNew(my_f_name="Vadim"))

def test_modify_contact_middle_name(app):
    app.contacts.modify_first_contact(AddNew(my_m_name="Fillipovich"))

def test_modify_contact_last_name(app):
    app.contacts.modify_first_contact(AddNew(my_l_name="Sharapov"))
