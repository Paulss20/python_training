from model.add_new import AddNew


def test_modify_contact_first_name(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(AddNew(my_f_name="Petruxa", my_m_name="Aleksandrovich", my_l_name="Pupkin"))
    else:
        app.contacts.modify_first_contact(AddNew(my_f_name="Vadim"))

def test_modify_contact_middle_name(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(AddNew(my_m_name="Ibragimovich"))
    else:
        app.contacts.modify_first_contact(AddNew(my_m_name="Fillipovich"))

def test_modify_contact_last_name(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(AddNew(my_l_name="Grachev"))
    else:
        app.contacts.modify_first_contact(AddNew(my_l_name="Sharapov"))
