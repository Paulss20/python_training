
from fixture.orm import ORMFixture
from model.group import Group
from model.add_new import AddNew


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_delete_contact_from_group(app, db):
     # собираем списки групп и контактов из БД, если они пусты, добавляем группу и контакт
     groups = db.get_group_list()
     contacts = db.get_contact_list()
     if len(groups) == 0:
         app.group.create(Group(name="group_to_delete"))
     if len(contacts) == 0:
         app.contacts.create_contact(AddNew(my_f_name="contact_to_delete"))

     # собираем список контактов, присутствующих в таблице связи групп и контактов через orm, если таковых нет, то создаем и добавляем
     old_dealed_contacts = orm.get_dealed_contacts()

     # если нет занятого контакта, то создаем контакт и группу и связываем их
     if len(old_dealed_contacts) == 0 :
         dealed_group = app.group.create(Group(name="group_to_delete"))
         dealed_contact = app.contacts.create_contact(AddNew(my_f_name="contact_to_delete"))
         # app.contacts.add_contact_to_group(old_free_contacts[0], old_free_groups[0])
         app.contacts.add_contact_to_group( dealed_contact, dealed_group)
         old_dealed_contacts = orm.get_dealed_contacts()

     dealed_contact = old_dealed_contacts[0]
     dealed_group = orm.get_groups_of_contact(dealed_contact)[0]

     app.contacts.remove_contact_from_group(dealed_contact, dealed_group)
     print("Contact with id %s from the group with id %s successfully deleted" % (dealed_contact, dealed_group))

     # собираем списки групп и контактов, отсутствующих в таблице связи групп и контактов через orm, после добавления
     new_dealed_contacts = orm.get_dealed_contacts()

     # проверяем, что список свободных контактов изменился на 1
     assert len(old_dealed_contacts) == len(new_dealed_contacts) + 1