
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

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    # binding to physical DB
    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)  # shows real sql - query

    # a list of objects of the "Groups" class is formed
    def convert_group_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    # need to mark the blocks of code that work with the database session. With (with "db_session:") - in the code
    # or (@db_session :) - before the whole function.
    @db_session
    def get_group_list(self):
        return self.convert_group_to_model(select(g for g in ORMFixture.ORMGroup))

    # a list of objects of the "Contacts" class is formed
    def convert_contact_to_model(self, contacts):
        def convert(contact):
            return AddNew(my_id=str(contact.id), my_f_name=contact.firstname, my_l_name=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contact_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))