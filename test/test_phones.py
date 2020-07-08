

def test_phones_on_home_page(app):
     contact_from_home_page = app.contacts.get_contact_list()[0]
     contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
     assert contact_from_home_page.my_h_telefon == contact_from_edit_page.my_h_telefon
     assert contact_from_home_page.my_mobile == contact_from_edit_page.my_mobile
     assert contact_from_home_page.my_work_telefon == contact_from_edit_page.my_work_telefon
     assert contact_from_home_page.my_secondary_phone == contact_from_edit_page.my_secondary_phone