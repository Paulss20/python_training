from model.add_new import AddNew
from random import randrange


def test_modify_contact_first_name(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(AddNew(my_f_name="Petruxa"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    contact = AddNew(my_l_name="Demidov", my_f_name="Vadim")
    contact.my_id = old_contacts[index].my_id
    app.contacts.modify_contact_by_index(index, contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=AddNew.id_or_max) == sorted(new_contacts, key=AddNew.id_or_max)


#def test_modify_contact_middle_name(app):
#    if app.contacts.count() == 0:
#        app.contacts.create_contact(AddNew(my_m_name="Ibragimovich"))
#    old_contacts = app.contacts.get_contact_list()
#    app.contacts.modify_first_contact(AddNew(my_m_name="Fillipovich"))
#    new_contacts = app.contacts.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_contact_last_name(app):
#    if app.contacts.count() == 0:
#        app.contacts.create_contact(AddNew(my_l_name="Grachev"))
#    old_contacts = app.contacts.get_contact_list()
#    app.contacts.modify_first_contact(AddNew(my_l_name="Sharapov"))
#    new_contacts = app.contacts.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

