
from model.add_new import AddNew


def test_contacts_on_homepage(app, db):
    contacts_from_homepage = sorted(app.contacts.get_contact_list(),  key = AddNew.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(),  key = AddNew.id_or_max)
    assert len(contacts_from_homepage) == len(contacts_from_db)

    for i in range(len(contacts_from_homepage)):
        assert contacts_from_homepage[i].my_f_name == contacts_from_db[i].my_f_name
        assert contacts_from_homepage[i].my_l_name == contacts_from_db[i].my_l_name
        assert contacts_from_homepage[i].my_home_address == contacts_from_db[i].my_home_address
        assert contacts_from_homepage[i].all_phones_from_home_page == contacts_from_db[i].all_phones_from_home_page
        assert contacts_from_homepage[i].all_emails_from_home_page == contacts_from_db[i].all_emails_from_home_page