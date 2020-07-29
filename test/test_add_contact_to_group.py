
from fixture.orm import ORMFixture
from model.group import Group
from model.add_new import AddNew


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db):
     # собираем списки групп и контактов из БД, если они пусты, добавляем группу и контакт
     groups = db.get_group_list()
     contacts = db.get_contact_list()
     if len(groups) == 0:
         app.group.create(Group(name="free_group"))
     if len(contacts) == 0:
         app.contacts.create_contact(AddNew(my_f_name="free_contact"))

     # собираем списки групп и контактов, отсутствующих в таблице связи групп и контактов через orm, если таковых нет, то создаем
     old_free_contacts = orm.get_free_contacts()
     old_free_groups = orm.get_free_groups()

     if len(old_free_groups) == 0:
         app.group.create(Group(name="free_group"))
         old_free_groups = orm.get_free_groups()

     if len(old_free_contacts) == 0:
         app.contacts.create_contact(AddNew(my_f_name="free_contact"))
         old_free_contacts = orm.get_free_contacts()

     # добавляем первый свободный контакт в первую свободную группу
     app.contacts.add_contact_to_group(old_free_contacts[0], old_free_groups[0])
     print("Contact with id %s has been successfully added to the group with id %s" % (old_free_contacts[0], old_free_groups[0]))

     # собираем списки групп и контактов, отсутствующих в таблице связи групп и контактов через orm, после добавления
     new_free_contacts = orm.get_free_contacts()
     new_free_groups = orm.get_free_groups()

     # проверяем, что список свободных групп и контактов изменился на 1
     assert len(old_free_contacts) == len(new_free_contacts) + 1
     assert len(old_free_groups) == len(new_free_groups) + 1