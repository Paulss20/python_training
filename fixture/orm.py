
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.add_new import AddNew
from pymysql.converters import decoders


class ORMFixture:

    db = Database()

    # classes describe the structure that will be written to the database
    class ORMGroup(db.Entity):
         _table_ = 'group_list'
         id = PrimaryKey(int, column='group_id')
         name = Optional(str, column='group_name')
         header = Optional(str, column='group_header')
         footer = Optional(str, column='group_footer')
         # применяем lanmda, так как класс контакты описан позже, описываем связывающую таблицу и поля
         # lazy = True - инфорация будет извелкаться только в момент обращения к этому свойству при
         # получении списка контактов
         contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups',
                        column='id', reverse='groups', lazy=True)


    class ORMContact(db.Entity):
         _table_ = 'addressbook'
         id = PrimaryKey(int, column='id')
         firstname = Optional(str, column='firstname')
         lastname = Optional(str, column='lastname')
         deprecated = Optional(datetime, column='deprecated')
         groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups',
                      column='group_id', reverse='contacts', lazy=True)

    # binding to physical DB
    def __init__(self, host, name, user, password):
         self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
         self.db.generate_mapping()
         sql_debug(True)  # shows real sql - query

    # a list of objects of the "Groups" class is formed
    def convert_groups_to_model(self, groups):
         def convert(group):
              return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
         return list(map(convert, groups))

    # need to mark the blocks of code that work with the database session. With (with "db_session:") - in the code
    # or (@db_session :) - before the whole function.
    @db_session
    def get_group_list(self):
         return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    # a list of objects of the "Contacts" class is formed
    def convert_contacts_to_model(self, contacts):
         def convert(contact):
             return AddNew(my_id=str(contact.id), my_f_name=contact.firstname, my_l_name=contact.lastname)
         return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
         return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
         orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
         return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
         orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
         return self.convert_contacts_to_model(
              select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))




