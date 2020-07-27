from model.add_new import AddNew
import random


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list())== 0:
        app.contacts.create_contact(AddNew(my_f_name="Petruxa"))
    old_contacts = db.get_contact_list()
    contact_old = random.choice(old_contacts)
    id = contact_old.my_id
    contact_new = AddNew(my_l_name="Demidov", my_f_name="Vadim", my_h_telefon="12121212121",
                        my_mobile="2323232323232", my_work_telefon="454545454545",
                        my_secondary_phone="656565656565", my_home_address="Nevskiy str, 123",
                        my_company_mail="bit_comp@ya.com", my_second_mail="bit2_comp@ya.com",
                        my_third_mail="bit3_comp@ya.com")
    contact_new.my_id = id
    app.contacts.modify_contact_by_id(id, contact_new)
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].my_id == id:
            old_contacts[i] = contact_new
    assert sorted(old_contacts, key=AddNew.id_or_max) == sorted(new_contacts, key=AddNew.id_or_max)

    if check_ui:    # for a disabled check, where we compare the database information with the UI,
                    # we need to transform the list taken from the database (we take only id and name)
         new_contacts_ui = []
         for i in new_contacts:
              new_contacts_ui.append(AddNew(my_l_name=app.contacts.removing_spaces(i.my_l_name),
                                            my_f_name=app.contacts.removing_spaces(i.my_f_name),
                                            my_id=i.my_id,
#                                            work_address=i.work_address,
                                            all_phones_from_home_page=app.contacts.merge_phones_like_on_home_page(i),
                                            all_emails_from_home_page=app.contacts.merge_emails_like_on_home_page(i)
                                            )
                                    )
         assert sorted(new_contacts_ui, key=AddNew.id_or_max) == sorted(app.contacts.get_contact_list(), key=AddNew.id_or_max)


