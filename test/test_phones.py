import re

def test_phones_on_home_page(app):
     contact_from_home_page = app.contacts.get_contact_list()[0]
     contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
     contact_from_view_page = app.contacts.get_contact_from_view_page(0)
     contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
     assert contact_from_view_page.my_h_telefon == contact_from_edit_page.my_h_telefon
     assert contact_from_view_page.my_mobile == contact_from_edit_page.my_mobile
     assert contact_from_view_page.my_work_telefon == contact_from_edit_page.my_work_telefon
     assert contact_from_view_page.my_secondary_phone == contact_from_edit_page.my_secondary_phone

def clear(s):
     return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contacts):
     return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                                           [contacts.my_h_telefon, contacts.my_mobile,
                                                            contacts.my_work_telefon, contacts.my_secondary_phone]))))