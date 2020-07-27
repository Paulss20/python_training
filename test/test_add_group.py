# -*- coding: utf-8 -*-
from model.group import Group
import re


def test_add_group(app, db, json_groups, check_ui):
     group = json_groups
     old_groups = db.get_group_list()
     app.group.create(group)
     new_groups = db.get_group_list()
     old_groups.append(group)
     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
     if check_ui:    # for a disabled check, where we compare the database information with the UI,
                     # we need to transform the list taken from the database (we take only id and name)
          new_groups_ui = []
          for i in new_groups:
               new_groups_ui.append(Group(id=i.id, name=re.sub("  ", " ", i.name.strip())))
          assert sorted(new_groups_ui, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




