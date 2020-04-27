# -*- coding: utf-8 -*-
from model.add_new import AddNew


def test_add_new(app):
     old_contacts = app.contacts.get_contact_list()
     contact = AddNew(my_f_name="Sergei", my_m_name="Fedorovich", my_l_name="Semenov", my_nickname="try",
                                       my_company="Big company", work_address="SPb, Fuchika str, 15", my_h_telefon="11111111",
                                       my_mobile="2222222222", my_work_telefon="3333333333", my_fax="4444444444",
                                       my_company_mail="big.company@gg.com", my_second_mail="b_company@gg.com",
                                       my_homepage="www.big-company.su", my_byear="1985", my_home_address="SPb, Nevski str, 98",
                                       my_second_address="SPb, Pushkin, Gogol str, 87", my_notes="fff")
     app.contacts.create_contact(contact)
     assert len(old_contacts) + 1 == app.contacts.count()
     new_contacts = app.contacts.get_contact_list()
     old_contacts.append(contact)
     assert sorted(old_contacts, key=AddNew.id_or_max) == sorted(new_contacts, key=AddNew.id_or_max)



#def test_add_empty_new(app):
#     old_contacts = app.contacts.get_contact_list()
#     app.contacts.create_contact(AddNew(my_f_name="", my_m_name="", my_l_name="", my_nickname="",
#                                       my_company="", work_address="", my_h_telefon="",
#                                       my_mobile="", my_work_telefon="", my_fax="",
#                                       my_company_mail="", my_second_mail="",
#                                       my_homepage="", my_byear="", my_home_address="",
#                                       my_second_address="", my_notes=""))
#     new_contacts = app.contacts.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)

